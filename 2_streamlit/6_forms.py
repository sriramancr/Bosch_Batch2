# A Streamlit form groups multiple input widgets together and waits until the user clicks Submit before processing the values.

# Without a form, every widget interaction causes the entire script to rerun. 
# With a form, the script reruns only when the form is submitted.

# Advantages of using forms
#   * Single submission
#   * All inputs are submitted together.
#   * Prevents partial or incomplete processing.
#   * Better performance
#   * Avoids rerunning expensive operations every time a user types or changes a widget.
#   * Better user experience
#   * Users can complete all fields before validation or processing begins.
#   * Easier validation
#   * Validate all fields together after the Submit button is clicked.

# -*- coding: utf-8 -*-

import streamlit as st, spacy, time

# -----------
# page design
# ------------
st.set_page_config(layout='wide')

nlp = spacy.load("en_core_web_sm")

def extract_entities(ent_types,text):
    results = []
    
    doc = nlp(text)
    
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append(f"{ent.text} : {ent.label_}")
    return(results)
    
    
form1 = st.form(key="frm_Entities")
form1.header("NLP - NER[Named Entity Recognition]")

c1,c2,c3,c4 = form1.columns([0.4,0.4,0.1,0.1])

ent_types = c1.multiselect("Select Entities", ["GPE","PERSON","ORG","DATE","MONEY"])

t = "India has Industries worth $50 Billion in Gujarat, Tamilnadu. Modi is a visionary. It started in May, 2014"
text = c2.text_area("Sample Text", t)
btn_get = c3.form_submit_button("Get")
btn_close = c4.form_submit_button("Close")

if btn_get:
    if len(ent_types) <= 0:
        st.error("Select at least 1 entity to retrieve")
    else:
        with st.spinner("Getting entities..."):
            hits = extract_entities(ent_types, text)
        
            st.write(hits)
    
if btn_close:    
    with (st.spinner("Closing application ...")):
        import os, keyboard, psutil
        
        time.sleep(1)
        keyboard.press_and_release('ctrl+w')
        pid = os.getpid()
        p = psutil.Process(pid)
        p.terminate()