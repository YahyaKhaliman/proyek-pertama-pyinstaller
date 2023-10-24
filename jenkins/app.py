import subprocess
import time

# Build the Node.js/React application
print("Building the Node.js/React application...")
subprocess.call(["npm", "run", "build"], cwd="/var/jenkins_home/workspace/simple-node-js-react-app", shell=True)

# Start the Node.js/React application in development mode
print("Starting the Node.js/React application in development mode...")
start_process = subprocess.Popen("npm start &", cwd="/var/jenkins_home/workspace/simple-node-js-react-app", shell=True, preexec_fn=os.setsid)

# Wait for a moment to ensure the application is up and running
time.sleep(1)

# Write the process ID (PID) to a file
with open(".pidfile", "w") as pidfile:
    pidfile.write(str(start_process.pid))

print("The Node.js/React application is running. You can visit http://localhost:3000 to see it in action.")
