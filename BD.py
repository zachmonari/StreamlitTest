import streamlit as st
import PIL.Image as Image

logo=Image.open("ZachTechs.jpg")
st.image(logo,width=150)

st.header("SURPRISE!")
click=st.button("Click here")
if click:
    st.balloons()
    st.markdown("Here's a bouquet for you bbg &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    # ---- Header ----
    st.title("🌸 Happy Birthday, My Love 💖")
    st.subheader("To the girl who makes every day feel like a celebration of love.")
