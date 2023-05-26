import openai
import os
import streamlit as st
openai.api_key = os.getenv("apikey")
def getresponse(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Explain this topic " + topic + "in a "
                                                                              "simple words in 5 to 6 lines"}]
    )
    reply = response.choices[0].message.content
    return reply
css = """
<style>
h1{ color : red;}
</style>
"""
st.markdown(css,unsafe_allow_html=True)
st.title("Simplipedia\n")
st.text("Simplipedia is used to explains the hard topics in a simple manner.\n")
topic = st.text_input("Enter the topic: ")
if topic:
    st.write(getresponse(topic))
link = "https://docs.google.com/forms/d/e/1FAIpQLSfwFzEbKYFAHe3M2XYrBYYBAf0z1T2GGvD0T1dB2RQdlzoarw/viewform?usp=sf_link"
button_label = "Feedback"
if(st.button(button_label)):
    st.markdown(f'<a href = "{link}" target = "_blank">{button_label}</a>',unsafe_allow_html=True)
