# %%
import streamlit as st
import requests
import time

st.title("MHADA FCFS Alert System")

URL = "https://bookmyhome.mhada.gov.in/app/select-scheme/3/161/APPLY"

if st.button("Check Now"):
    response = requests.get(URL)
    
    if "Available" in response.text:
        st.success("⚡ Flat Available!")
    else:
        st.warning("No flats right now")

st.info("Click button to manually check availability")


