import streamlit as st
from PIL import Image

import stutils

st.set_page_config(page_title="ARQAN", page_icon="🤖")

st.title("ARQAN. NLP-automated Requirements Analysis 🤖")

stutils.loginbar()

# Use a layout with two columns
col1, col2 = st.columns(2)

# Load images/icons
stig_image = Image.open("./utils/stigsearch.png")
security_image = Image.open("./utils/secreq.png")

# Prototype 1: STIG Search
with col1:
    st.image(stig_image, width=101)  # Adjust the width as needed
    st.header("STIG Search")
    st.write("""
    For a given textual security requirement and a specific platform (e.g., Windows 10),
    this tool searches relevant Security Technology Implementation Guidelines (STIG).
    It provides a recipe for detailed security requirements or even a fix.
    """)
    st.page_link("pages/1_STIG_Search.py", label="STIG Search", icon="🔍")

# Prototype 2: Security Requirements Extraction
with col2:
    st.image(security_image, width=150)  # Adjust the width as needed
    st.header("SecReq Extraction")
    st.write("""
    Upload a PDF file, and this tool will analyze it to extract security-related requirements.
    It is designed to identify and present specific security needs found within the document.
    """)
    st.page_link("pages/2_RSecReq_Extraction.py", label="SecReq Extraction", icon="📤")

# Optionally, add a footer or additional information
st.markdown("---")
st.write("Select one of the tools above to start using them.")