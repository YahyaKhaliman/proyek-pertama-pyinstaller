#!/bin/sh

echo 'Menjalankan aplikasi Python Anda dengan Flask:'
set -x

# Pastikan Anda memiliki Flask diinstal dalam environment Python Anda
pip install Flask

# Jalankan aplikasi Python Anda
python sources/app.py &

# Tunggu sebentar untuk memastikan aplikasi selesai berjalan
sleep 1

# Simpan ID proses yang berjalan di dalam berkas .pidfile
echo $! > .pidfile

set +x

echo 'Sekarang...'
echo 'Kunjungi http://localhost:5000 untuk melihat aplikasi Python Anda beraksi.'
