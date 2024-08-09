import json
import time
from collections import defaultdict
from http import HTTPStatus

import numpy as np
import pandas as pd
import streamlit as st

import stutils
from client.types import File
from client import AuthenticatedClient
from client.api.common.get_task import sync as tasksync
from client.api.common.get_task import sync_detailed as tasksync_detailed
from client.api.extract_sec_req import extract_from_pdf
from client.models.body_extract_from_pdf import BodyExtractFromPdf as Body
from client.models.request_extract_from_pdf import ExtractFromPDFRequest

st.set_page_config(page_title="ARQAN. Security Requirements Extraction", page_icon="📤")

st.title("ARQAN. Extract security requirements from a PDF 📤")

stutils.loginbar()

st.write(
    """
    Upload a PDF file, and this tool will analyze it to extract security-related requirements.
    It is designed to identify and present specific security needs found within the document.
    """
)


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


uploaded_file = st.file_uploader("Choose a security specification PDF file:")

_but = st.button("Extract security requirements")


def pass_init_check():
    if uploaded_file is None:
        st.error("Error: please upload PDF first")
        return False
    if not st.session_state.get("token"):
        st.error("Error: token is emply. Please log in.")
        return False
    if st.session_state.get("token") == "":
        st.error("Error: token is emply. Please log in.")
        return
    return True


if _but:
    if pass_init_check():
        acl = AuthenticatedClient(
            base_url="https://arqan.softeam-rd.eu/",
            token=st.session_state.token,
            verify_ssl=False,
        )
        with acl as cl:
            some = ExtractFromPDFRequest()
            file_obj = File(
                payload=uploaded_file,  # The file-like object
                file_name=uploaded_file.name,  # The name of the file
                mime_type=uploaded_file.type,  # The MIME type of the file
            )
            # f = File(uploaded_file)
            b = Body(file=file_obj, sec_req_extract=some)
            r = extract_from_pdf.sync_detailed(client=acl, body=b)

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

                    st.write("### Extracted requirements:")
                    st.markdown("\n".join([f"1. {req}" for req in r2["requirements"]]))
                    print(r2)
