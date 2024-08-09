import time
from collections import defaultdict

from http import HTTPStatus

import streamlit as st
import stutils
from client import AuthenticatedClient
from client.api.common.get_task import sync as tasksync
from client.api.common.get_task import sync_detailed as tasksync_detailed
from client.api.stig_search import search_db
from client.models.request_search_db import SearchDBRequest

st.set_page_config(page_title="ARQAN. STIG Search", page_icon="📈")

st.title("ARQAN. Recommend relevant STIGs for a requirement 📈")

stutils.loginbar()


# Function to wait for task completion
def wait_for_task_completion(client, task_id, delay=0.1):
    while True:
        result = tasksync(client=client, task_id=task_id)
        if result is not None:
            return result
        time.sleep(delay)


# Process the data
def show_requirements(data):
    stig_requirements = data.get("stig", [])

    for requirement in stig_requirements:
        main_id = requirement.get("id")
        main_title = requirement.get("title")
        main_description = requirement.get("description")
        main_url = requirement.get("url")
        similar_requirements = requirement.get("similar_requirements", [])

        exp = st.expander(f"[{main_id}]({main_url}). {main_title}")
        exp.write(main_description)

        if similar_requirements:
            exp.write("_Similar Requirements:_")
            # Create a dictionary to group titles with their IDs
            title_dict = defaultdict(list)
            for similar in similar_requirements:
                sim_id = similar.get("id")
                sim_title = similar.get("title")
                sim_url = similar.get("url")
                title_dict[sim_title].append(f"[{sim_id}]({sim_url})")
            for title, ids in title_dict.items():
                exp.write(f"  - _{title} ({', '.join(ids)})_")


if not st.session_state.get("input_req"):
    st.session_state.input_req = ""
st.session_state.input_req = st.text_input(
    "Enter a requirement:", st.session_state.input_req
)

if not st.session_state.get("stig_platform"):
    st.session_state.stig_platform = "windows_10"
st.session_state.stig_platform = st.text_input(
    "Enter a STIG platform:",
    st.session_state.stig_platform,
    help="windows_10 or ubuntu or others",
)

if not st.session_state.get("search_limit"):
    st.session_state.search_limit = 10
# st.session_state.search_limit = st.slider(
#     "Search limit:",
#     value=st.session_state.search_limit,
#     step=1,
#     min_value=1,
#     max_value=10,
#     help="10",
# )

# print("TEST TEST TEST ")
# print("st.session_state.search_limit")
# print(st.session_state.search_limit)
# print(type(st.session_state.search_limit))


def pass_init_check():
    if st.session_state.input_req == "":
        st.error("Error: Empty requirement text.")
        return False
    if not st.session_state.get("token"):
        st.error("Error: token is emply. Please log in.")
        return False
    if st.session_state.get("token") == "":
        st.error("Error: token is emply. Please log in.")
        return
    return True


_but = st.button("Find")

if _but:
    if pass_init_check():
        acl = AuthenticatedClient(
            base_url="https://arqan.softeam-rd.eu/",
            token=st.session_state.token,
            verify_ssl=False,
        )

        with acl as cl:
            b = SearchDBRequest(
                text=st.session_state.input_req,
                platform=st.session_state.stig_platform,
                limit=st.session_state.search_limit,
            )
            r = search_db.sync_detailed(client=acl, body=b)

            # print("TEST TEST TEST ")

            # print(r)

            if r.status_code != HTTPStatus.OK:  # 200
                st.error("Server call failed")
                st.error(f"Status: {r.status_code.description}")
                if r.status_code == HTTPStatus.UNAUTHORIZED:  # 200
                    st.error("Renew token with Login")
                    st.session_state.token = ""
            else:
                task_id = r.parsed["task_id"]

                with st.spinner("Wait for it..."):
                    r2 = wait_for_task_completion(acl, task_id, 0.1)

                    # print(r2)

                    show_requirements(r2)
