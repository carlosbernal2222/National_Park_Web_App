import streamlit as st
from datetime import date, time
import pandas as pd
import numpy as np
import time as tm
import pydeck as pdk
import plotly.express as px

st.set_page_config(
    page_title="National_Park_WebApp",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a bug': 'https://www.gregoryreis.com',
        'About': '# Welcome to HCI. Developed by Gregory Murad Reis'
    }
)

# Header
st.title("Title Here")
st.header("Header Here")

add_selectbox = st.sidebar.selectbox("Select a Feature",
                                     ["Feature-1", "Feature-2", "Feature-3",
                                      "Feature-4"])

if add_selectbox == "Feature-1":
    st.write("To be Constructed")
    #Code for the feature needs to be in different file and imported to the app

elif add_selectbox == "Feature-2":
    st.write("To be Constructed")
    # Code for the feature needs to be in different file and imported to the app

elif add_selectbox == "Feature-3":
    st.write("To be Constructed")
    # Code for the feature needs to be in different file and imported to the app

elif add_selectbox == "Feature-4":
    st.write("To be Constructed")
    # Code for the feature needs to be in different file and imported to the app

else:
    st.subheader("This is the Home Page")
    #Home Page Content Here

