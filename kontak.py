import streamlit as st

def tampilkan_kontak():
    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/noviaanggitaaprilianti)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/novianggita)"
    )

    # Email
    st.write("📧 Email: noviaanggita047@gmail.com")

