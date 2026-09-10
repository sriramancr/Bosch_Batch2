import streamlit as st
import keyboard,psutil,os
import time, random, math

# -----------
# page design
# ------------
st.set_page_config(layout='wide')

st.header("5. Status Elements")

if (st.button("Exit")):
    keyboard.press_and_release('ctrl+w')
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()

st.divider()

st.success("SUCCESS: All updates have been done successfully", icon="💚")
st.info('INFO: This information is confidential', icon="🔑")
st.error("ERROR: Could not retrieve the Product details", icon="😱")
st.warning("WARNING: The current version will be deprecated on or before 31-12-2026. Upgrade to use the latest features", icon="⚠️")

import time

if st.button("Calculate"):
    data = []
    with st.spinner("Calculating ..."):
        for i in range(20):
            rnd = random.randint(25000,50000)
            st.toast(f"Random number : {rnd}")
            ans = rnd + math.sqrt(rnd) + math.log(rnd)
            time.sleep(0.25)
            data.append(ans)

    st.success("Data loaded!")

st.divider()
st.subheader("Thats all Folks ....!!!!")
st.snow()