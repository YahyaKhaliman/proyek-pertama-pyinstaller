#!/bin/sh

echo 'The following command runs your Python application:'

set -x

python sources/app.py &

sleep 1
echo $! > .pidfile
set +x

echo 'Now...'
echo 'Visit http://localhost:5000 to see your Python application in action.'
