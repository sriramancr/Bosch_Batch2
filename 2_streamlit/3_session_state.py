# pip install streamlit
# pip install streamlit-extras
# pip install keyboard

import streamlit as st
import keyboard,psutil,os,random

# -----------
# page design
# ------------
st.set_page_config(layout='wide')

# --------------
# session states
# ---------------
if "far" not in st.session_state:
    st.session_state["far"] = None


c1,c2 = st.columns(2)

c1.header("3. Session State")
if (c1.button("Exit")):
    keyboard.press_and_release('ctrl+w')
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()
    
msg = ''' Session State is a powerful feature that allows you to persist data across reruns of your application. 
This is useful for creating dynamic and interactive applications where user inputs or intermediate states need to be retained.

Session State behaves like a Python dictionary, enabling you to store and retrieve variables. 
'''
c2.write(msg)

centi = c1.number_input("Enter Degree")
f1 = c1.button("Convert degrees to Farenheit")
f2 = c1.button("Convert Farenheit to Centigrade")

if f1:
    far = ((9*centi)+160)/5
    st.write(f"Degree = {centi}, Farenheit = {far}")
    st.session_state["far"] = far

if f2:
    far = st.session_state["far"]
    if far is not None:
        centi = ((5*far)-160)/9
        st.write(f"Farenheit = {far}, Degree = {centi}")
    else:
        st.write("Cannot convert Degree to Farenheit")
    
# ------------------------------------------------------------------------------------------------------------

st.divider()

st.subheader("Sample Application")

def update_product_info():
    st.session_state.pid = str(random.randint(100,1000))
    st.session_state.pprice = str(random.randint(10,25000))
    

c1,c2,c3,c4 = st.columns(4)
pid = c1.text_input("Product ID",key="pid")
pname = c2.text_input("Product Name",key="pname")
pdesc = c3.text_input("Product Description",key="pdesc")
pprice = c4.text_input("Product Price",key="pprice")

if st.button("Show values"):
    st.write(st.session_state.pid)
    st.write(st.session_state.pname)
    st.write(st.session_state.pdesc)
    st.write(st.session_state.pprice)

st.button("Update values", on_click=update_product_info)
