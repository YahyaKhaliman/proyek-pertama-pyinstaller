#!/bin/sh

# Ganti '/usr/bin/python3' dengan path ke interpreter Python Anda
PYTHON_EXECUTABLE="/usr/bin/python3"

echo 'The following command runs your Python application:'

set -x

# Menggunakan path Python yang telah ditentukan
$PYTHON_EXECUTABLE sources/app.py &

sleep 1
echo $! > .pidfile
set +x

echo 'Now...'
echo 'Visit http://localhost:5000 to see your Python application in action.'
