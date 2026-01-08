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

    st.write("Songs for your birthday...")
    col1, col2 ,col3= st.columns(3, vertical_alignment="bottom", border=False)

    with col1:
        st.audio("Wadosi.mp3", format="audio/wav", loop=False)
        image = Image.open("Us.jpg")
        st.image(image, caption="My amazing bbg💞", width=325)
    with col2:
        st.audio("Busy.mp3", format="audio/wav", loop=False)
        image = Image.open("us 3.jpg")
        st.image(image, caption="One of the beautiful moments 💞", width=300)
    with col3:
        st.audio("Harmonize.mp3", format="audio/wav", loop=False)
        image = Image.open("us 4.jpg")
        st.image(image, caption="My beautiful reason to smile 💞", width=325)

    # Love message
    st.markdown("""
    <div class="love-box">
    <p>
    Today is a special day because it celebrates the most beautiful soul in my life — <b>you❤️</b>.
    </p>

    <p>
    From the moment you came into my life, everything changed for the better.
    Your smile brightens my darkest days, your kindness inspires me,
    and your love gives me peace I never knew I needed.
    </p>

    <p>
    On your birthday, I want you to know how deeply loved and appreciated you are.
    I am grateful for every memory we share and excited for every moment yet to come.
    </p>

    <p>
    May this new year bring you happiness, success, good health, and endless reasons to smile.
    I promise to stand by you, support you, and love you more with each passing day.
    </p>

    <p style="text-align:center;"><b>I love youuuuu❤️❤️</b></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        ### 🌹 My Dearest Candy,
        A new year begins, and my heart is full of gratitude for you.  
        Thank you for being my source of joy, strength, and endless inspiration.  
        You’ve brought warmth and purpose into my world, and I’m so lucky to have you by my side.  

        May this new year bring you peace, happiness, and countless reasons to smile.  
        You deserve the best of everything and I’ll always be here cheering you on. 💖
        """)
    st.markdown("""
        ---
        **Forever Yours,**  
        ✨ *Zach* ✨
        """)

st.caption("© 2026 ZachTechs")