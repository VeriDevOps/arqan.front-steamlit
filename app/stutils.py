import streamlit as st
from http import HTTPStatus

from client import Client
from client.api.authentication import sign_in
from client.models.body_sign_in import BodySignIn
from client.models.token import Token
from client.types import Response

if not st.session_state.get("token"):
    st.session_state.token = ""


def stlogin():
    if not st.session_state.get("user"):
        st.session_state.user = ""

    st.session_state.user = st.sidebar.text_input("User:", st.session_state.user)
    pwd = st.sidebar.text_input("Password:", type="password")

    _but = st.sidebar.button("Login", key="loginbar")

    if _but:
        response = Response(
            status_code=HTTPStatus.UNAUTHORIZED,  # Default status code, for example
            content=b"",  # Empty bytes
            headers={},  # Empty dictionary for headers
            parsed=None,  # None for the parsed attribute
        )

        cl = Client(base_url="https://arqan.softeam-rd.eu/", verify_ssl=False)

        with cl as client:
            body = BodySignIn(username=st.session_state.user, password=pwd)
            response: Response[Token] = sign_in.sync_detailed(client=client, body=body)
            if response.status_code != 200:
                st.sidebar.error("Error: Login failed. Check username and password.")
                st.sidebar.error(F"Status: {response.status_code.description}")
            else:
                st.session_state.token = response.parsed.access_token
                st.sidebar.success("You have logged in successfully")


def loginbar():
    if not st.session_state.get("token"):
        st.session_state.token = ""

    if (st.session_state.token == ""):
        st.sidebar.error("Please login")
        stlogin()
    else:
        st.sidebar.success(f"{st.session_state.user} is logged in")
        _but = st.sidebar.button("Renew token")
        if _but:
            st.session_state.token = ""
            stlogin()
