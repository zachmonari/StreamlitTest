import streamlit as st
from PIL import Image

logo=Image.open("ZachTechs.jpg")
st.image(logo, width=150)
st.title('My Favorite Person, Candy')

st.header("Surprise!")
click=st.button("Click here")
if click:
    st.balloons()
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.write("A song for you when you feel down")
st.audio("Close.mp3", format="audio/wav", loop=False)
st.write("Favorite song for us")
st.audio("PerfectDesign.mp3", format="audio/wav", loop=False)
st.write("Favorite song by Ed Sheeran")
st.audio("PerfectEd.mp3", format="audio/wav", loop=False)