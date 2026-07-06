import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/random_forest.pkl")

st.title("Prediksi Kelulusan Mahasiswa")

umur = st.number_input("Umur",18,35,20)
ips1 = st.number_input("IPS Semester 1",0.0,4.0,3.0)
ips2 = st.number_input("IPS Semester 2",0.0,4.0,3.0)
kehadiran = st.slider("Kehadiran",0,100,85)
sks = st.number_input("Jumlah SKS",0,24,20)

if st.button("Prediksi"):

    data = np.array([[umur,ips1,ips2,kehadiran,sks]])

    hasil = model.predict(data)

    if hasil[0]==1:
        st.success("Lulus Tepat Waktu")
    else:
        st.error("Berpotensi Terlambat")
