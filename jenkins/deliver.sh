#!/bin/sh

echo 'Menjalankan aplikasi Python di port 5000...'

# Instal dependensi Streamlit
pip install streamlit

# Jalankan aplikasi Streamlit
streamlit run nama_app_streamlit.py


# Menjalankan aplikasi Python di latar belakang
python sources/app.py &

# Menyimpan ID proses ke dalam file .pidfile
echo $! > .pidfile

echo 'Aplikasi sekarang berjalan. Kunjungi http://localhost:5000 untuk melihatnya.'
