
import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <img src="{logo_url}" style="height: 100px; width: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style="
            text-align: center;
            color: #E0E3FF;
            font-size: 48px;
            margin-top: 0;
        ">SNAP<br>CLASS</h1>
        """,
        unsafe_allow_html=True
    )
def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div style="text-align: center; gap: 10px;">
            <img src="{logo_url}" style="height:85px; width: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h2 style="
            text-align: center;
            color: #5865F2;
            font-size: 48px;
            margin-top: 0;
        ">SNAP<br>CLASS</h2>
        """,
        unsafe_allow_html=True
    )
