# pip install streamlit
# pip install streamlit-extras
# pip install keyboard

import streamlit as st
import datetime, os
from pathlib import Path
import keyboard,psutil,numpy as np

# -----------
# page design
# ------------
st.set_page_config(layout='wide')
st.markdown("""
<style>
.stApp {
    background-color:  #F8F9FA;
}
</style>
""", unsafe_allow_html=True)

st.header("2. Input Widgets")
if (st.button("Exit")):
    

    keyboard.press_and_release('ctrl+w')
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()

st.divider()

# columns: spanning the spaces

c1,c2,c3,c4 = st.columns(4)
c1.write("column 1")
c2.write("column 2")
c3.write("column 3")
c4.write("column 4")

# string input
s1 = c1.text_input("String 1")
s2 = c2.text_input("String 2")
s3 = c3.text_input("String 3")
s4 = c4.text_input("String 4")

c1.write(s1); c2.write(s2); c3.write(s3); c4.write(s4)


s5 = c1.text_area("Enter Description",value="This is a Text Area")
s6 = c2.number_input("Enter Score", min_value=1, max_value=100)
s7 = c1.selectbox("Educational Qualifications", ["School","High School","Graduate","Post Graduate","Diploma","Others"])
s8 = c1.multiselect("Select skills", ["AI","Programming","Project Management","Program Management","Enterpreneurship",
                                        "Data Science","Analytics","Analysis","Design & Development","Testing"])
                                        
s9 =   c2.checkbox("I have read the terms and conditions")
s10 = c3.radio("Select the algorithm to build the model",["Logistic Regression", "Decision Tree", "Random Forest", "SVM Classifier"])
s11 = c1.toggle("Show / Hide Parameters")

s12 = c2.select_slider("Select background colour", ["Red","Blue","Green","White","Black","Orange","Yellow","Indigo","Grey","Pink"])
s12 = c3.select_slider("Select Weight",np.round(np.linspace(0.01,1,25),2))

s13 = c1.date_input("Contract Date")

sel_file = c1.file_uploader("Select File",type=["csv","xlsx"])
if sel_file is not None:
    st.write(f"Selected File: {sel_file.name}")

st.divider()