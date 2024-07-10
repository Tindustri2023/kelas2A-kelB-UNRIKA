import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="UNRIKA 2023",
   page_icon="😎",
)
st.title("Project Teknik Industri<2A> INDEX UNRIKA")
st.write ("--------------------------")
st.sidebar.success("silahkan dipilih,")

with st.sidebar : 
    selected = option_menu ('Mengitung Volume Bangun Ruang',
                            ['Menghitung Volume Kubus',
                             'Menghitung Volume Balok',
                             'Menghitung Volume Tabung',
                             'Menghitung Volume Kerucut',
                             'Menghitung Volume Bola'],
                             default_index=0)
    
if (selected == 'Menghitung Volume Kubus') : 
    st.title('Menghitung Volume Kubus')
    panjang_sisi = st.slider ("masukan panjang sisi",0.0,100.0)
    hitung = st.button ("hitung volume")
    
    if hitung : 
        volume = panjang_sisi * panjang_sisi * panjang_sisi
        st.success (f"volume Kubus adalah = {volume}")

if (selected == 'Menghitung Volume Balok') : 
    st.title('Menghitung Volume Balok')
    panjang = st.slider ("masukan nilai panjang", 0.0 , 100.0)
    lebar = st.slider ("masukan nilai lebar", 0.0 , 100.0)
    tinggi = st.slider ("masukan nilai tinggi", 0.0 , 100.0)
    hitung = st.button ("hitung volume")

    if hitung : 
        volume = panjang * lebar * tinggi
        st.success (f"volume Balok adalah = {volume}")
        

if (selected == 'Menghitung Volume Tabung') : 
    st.title('Menghitung Volume Tabung')
    r = st.slider ("masukan nilai jari-jari",0.0,100.0)
    tinggi = st.slider ("masukan nilai tinggi",0.0,100.0)
    hitung = st.button ("hitung volume")
    phi = 3.14
    if hitung : 
        volume = phi * r * r * tinggi
        st.success (f"volume Tabung adalah = {volume}")

if (selected == 'Menghitung Volume Kerucut') : 
    st.title('Menghitung Volume Kerucut')
    alas = st.slider ("masukan luas alas",0.0,100.0)
    tinggi = st.slider ("masukan tinggi",0.0,100.0)
    syarat = 1/3
    hitung = st.button ("hitung volume")
    
    if hitung : 
        volume = syarat * alas * tinggi
        st.success (f"volume Kerucut adalah = {volume}")

if (selected == 'Menghitung Volume Bola') : 
    st.title('Menghitung Volume Bola')
    r = st.slider ("masukan nilai jari-jari", 0.0 , 100.0)
    phi = 3.14
    ball = 4/3
    hitung = st.button ("hitung volume")

    if hitung : 
        volume = r * phi * ball * r * r
        st.success (f"volume Bola adalah = {volume}")        