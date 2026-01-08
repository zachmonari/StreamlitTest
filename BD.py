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

    col1, col2 ,col3= st.columns(3, vertical_alignment="bottom", border=False)
    st.write("Songs for your birthday...")
    with col1:
        st.audio("Wadosi.mp3", format="audio/wav", loop=False)
        image = Image.open("PH2.jpg")
        st.image(image, caption="My amazing bbg💞", width=325)
    with col2:
        st.audio("Busy.mp3", format="audio/wav", loop=False)
        image = Image.open("PH1.jpg")
        st.image(image, caption="One of the beautiful moments 💞", width=325)
    with col3:
        st.audio("Harmonize.mp3", format="audio/wav", loop=False)
        image = Image.open("PH2.jpg")
        st.image(image, caption="My beautiful reason to smile 💞", width=325)