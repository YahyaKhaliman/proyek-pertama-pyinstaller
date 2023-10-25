#!/bin/sh

echo 'Menjalankan aplikasi Python di port 5000...'

# Instal dependensi Streamlit
pip install streamlit

# Menjalankan aplikasi Python di latar belakang
python sources/app.py &

echo 'Aplikasi sekarang berjalan. Kunjungi http://localhost:5000 untuk melihatnya.'
