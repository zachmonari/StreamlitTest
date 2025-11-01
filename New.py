import streamlit as st
import PIL.Image as Image

logo=Image.open("ZachTechs.jpg")
st.image(logo,width=150)

# ---- Page Setup ----
st.set_page_config(page_title="Happy New Month My Love 💖", page_icon="💞", layout="centered")

st.header("Surprise!")
click=st.button("Click here")
if click:
    st.balloons()
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    # ---- Header ----
    st.title("🌸 Happy New Month, My Love 💖")
    st.subheader("To the girl who makes every day feel like a celebration of love.")

    # ---- Image Section ----
    col1, col2 = st.columns(2, vertical_alignment="bottom", border=False)
    st.write("A song for you...")
    st.audio("PerfectEd.mp3", format="audio/wav", loop=False)
    with col1:
        image = Image.open("PH2.jpg")
        st.image(image, caption="My beautiful reason to smile 💞", width=325)
    with col2:
        image = Image.open("PH1.jpg")
        st.image(image, caption="One of the beautiful moments 💞", width=325)


    # ---- Appreciation Message ----
    st.markdown("""
    ### 🌹 My Dearest Candy,
    A new month begins, and my heart is full of gratitude for you.  
    Thank you for being my source of joy, strength, and endless inspiration.  
    You’ve brought warmth and purpose into my world, and I’m so lucky to have you by my side.  

    May this new month bring you peace, happiness, and countless reasons to smile.  
    You deserve the best of everything — and I’ll always be here cheering you on. 💖
    """)

    # ---- Love Note Section ----
    st.markdown("""
    ### 💌 My Love Note
    If I could write every reason why I appreciate you,  
    I’d need more than just a lifetime.  
    You’re my favorite chapter, my calm in chaos, and my sweetest blessing.  
    Happy New Month, my love — let’s make more beautiful memories together. 💞
    """)

    # ---- Footer ----
    st.markdown("""
    ---
    **Forever Yours,**  
    ✨ *Zach* ✨
    """)

st.caption("© 2025 ZachTechs")

