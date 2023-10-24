import subprocess
import time

# Build your Node.js/React application for production
print("Building your Node.js/React application for production...")
subprocess.call(["npm", "run", "build"])

# Run your Node.js/React application in development mode
print("Running your Node.js/React application in development mode...")
start_process = subprocess.Popen("npm start &", shell=True, preexec_fn=os.setsid)

# Wait for a moment to ensure the application is up and running
time.sleep(1)

# Write the process ID (PID) to a file
with open(".pidfile", "w") as pidfile:
    pidfile.write(str(start_process.pid))

print("Now...")
print("Visit http://localhost:3000 to see your Node.js/React application in action.")
