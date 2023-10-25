import streamlit as st

st.write("""
SUBMISSION CI/CD DICODING 2023
""")

a = st.number_input("Masukkan Alas : ", 0)
t = st.number_input("Masukkan Tinggi : ", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = 0.5 * a * t
    st.success("Luas Segitiga adalah {}".format(luas))
    st.balloons()
