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

st.set_page_config(page_title="For My Love ❤️", page_icon="💞", layout="centered")

# Header
st.title("💖 To My One and Only 💖")
st.subheader("A small app to show how much I love and appreciate you.")

# Image section
image = Image.open("Us.jpg")
st.image(image, caption="One of Our beautiful moments 💞", width=500)

# Love message
st.markdown("""
### 🌹 My Love Letter to You
From the moment we met, my world became brighter.  
Every laugh, every glance, every moment — means everything to me.  
You inspire me, comfort me, and make me believe in forever. ❤️  
""")

# Love meter
love = st.slider("How much do I love you?", 0, 100, 100)
if love == 100:
    st.success("💘 My love for you is infinite! 💘")

# Reasons section
st.markdown("### 🌸 Reasons I Love You:")
reasons = [
    "Your smile brightens my darkest days 😍",
    "You believe in me even when I doubt myself 💪",
    "You make ordinary moments feel magical ✨",
    "You have the kindest heart I’ve ever known 💖"
]
for r in reasons:
    st.write(f"- {r}")



col1, col2, col3 = st.columns(3,vertical_alignment="bottom")

with col1:
    st.header("Nature....")
    st.image("Nature1.jpg")
    st.write("A song for you...")
    st.audio("Close.mp3", format="audio/wav", loop=False)

with col2:
    st.header("Nice pic....")
    st.image("Nature2.jpg")
    st.write("Favorite song for us")
    st.audio("PerfectDesign.mp3", format="audio/wav", loop=False)

with col3:
    st.header("The sunset....")
    st.image("Nature3.jpg")
    st.write("Favorite song by Ed Sheeran")
    st.audio("PerfectEd.mp3", format="audio/wav", loop=False)

# Footer
st.markdown("""
---
### 💌 Forever Yours,
**Zach**
""")
st.caption("© 2025 ZachTechs")