from http import HTTPStatus

import streamlit as st
from client import Client
from client.api.authentication import sign_in
from client.models.body_sign_in import BodySignIn
from client.models.token import Token
from client.types import Response
import stutils

st.set_page_config(page_title="ARQAN. Login", page_icon="📈")

st.title("ARQAN. NLP-automated Requirements Analysis 📈")

if not st.session_state.get("user"):
    st.session_state.user = ""

st.session_state.user = st.text_input("Enter user name:", st.session_state.user)

pwd = st.text_input("Enter password:", type="password")

stutils.loginbar()


if not st.session_state.get("token"):
    st.session_state.token = ""


response = Response(
    status_code=HTTPStatus.UNAUTHORIZED,  # Default status code, for example
    content=b"",  # Empty bytes
    headers={},  # Empty dictionary for headers
    parsed=None,  # None for the parsed attribute
)

_but = st.button("Login")

if _but:
    cl = Client(base_url="https://arqan.softeam-rd.eu/", verify_ssl=False)

    with cl as client:
        body = BodySignIn(username=st.session_state.user, password=pwd)
        response: Response[Token] = sign_in.sync_detailed(client=client, body=body)
        if response.status_code != 200:
            st.write("Error:", response.status_code.description)
        else:
            st.session_state.token = response.parsed.access_token

st.write("User:", st.session_state.user)
st.write("Password:", pwd)
st.write("Response:", response)
st.write("Token:", st.session_state.token)

st.write("Status:", response.status_code)
st.write("description:", response.status_code.description)
