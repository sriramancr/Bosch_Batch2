import streamlit as st
import keyboard,psutil,os, numpy as np, pandas as pd

# -----------
# page design
# ------------
st.set_page_config(layout='wide')

c1,c2 = st.columns(2)

c1.header("4. Layouts & Containers")
if (c1.button("Exit")):
    keyboard.press_and_release('ctrl+w')
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()

with c1.container(border=True):
    st.caption("Container: Can hold multi-elements")
    st.write("Distribution of Energy over the past 50 days")

    # You can call any Streamlit command, including custom components:
    st.line_chart(np.random.randn(50, 1))
    
with c2.expander("What is a Prime Number. Click to see...."):
    st.caption("Expander")
    
    msg = '''
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is composite because it is a product (2 × 2) in which both numbers are smaller than 4.    
'''
    st.write(msg)


with c2.popover("Randomize Data"):
    st.write("This is a popover")
    name = st.text_input("Enter a random text !")
    st.write(name)
    
with st.bottom:
    st.caption("© 2026 Sriraman Rajagopalan · All rights reserved")
    
# --------------------------------------------------------------------------

tab1, tab2 = c1.tabs(["Display Image", "Show Text"])

with tab1:
    st.header("Image")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab2:
    st.write("This is tab 2 with a random text")