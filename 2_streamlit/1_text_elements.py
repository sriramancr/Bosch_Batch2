# pip install streamlit
# pip install streamlit-extras
# pip install keyboard

# import libraries
import streamlit as st
import datetime, os
from pathlib import Path
import keyboard,psutil

# -----------
# page design
# ------------
st.set_page_config(layout='wide')

# -------------
# Text Elements
# -------------

st.header("1. Text Elements") 
if (st.button("Exit")):
    keyboard.press_and_release('ctrl+w')
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()

st.divider() # draw a horizontal line


now = datetime.datetime.now()
today = now.strftime('%A') + ", " + now.strftime("%B %d, %Y")
# st.sidebar.button(today,icon="⏳")
st.sidebar.subheader("This is a Side Bar")
st.sidebar.write(today)

st.write("Welcome to Streamlit")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")

# mathematical formula
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


# Markdown is used in Streamlit to format text in various ways, such as headings, lists, links, and images. 
# It allows for the creation of visually appealing and organized content within the app. 
# The st.markdown() function is a key tool for this purpose, enabling developers to display formatted text easily.
st.markdown("# With markdown: Main page 🎈")
st.markdown("## with markdown: Sub page")
st.markdown("*Streamlit* is **really** ***cool***.") # *italic* **bold** ***bold+italic***

# colors for specific texts
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
    ''')
    
st.markdown("Here's a bouquet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# horizontal line divider
st.divider()

# Display a colored badge with an icon and label.
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
st.markdown(
    ":red-badge[:material/star: Top Selling] :orange-badge[⚠️ Medium Rated] :gray-badge[Low Sales]"
)

# Insert an HTML page
st.iframe(Path("D:/stackroute/2_AI-assisted-programming/learning_requirements/lloyds/2026/openai_code/templates/index.html"), width=400,height=600)

