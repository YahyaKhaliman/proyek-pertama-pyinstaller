import subprocess
import time

# Build the Node.js/React application
print("Building the Node.js/React application...")
subprocess.run(["npm", "run", "build"], cwd="/var/jenkins_home/workspace/simple-node-js-react-app")

# Start the Node.js/React application in development mode
print("Starting the Node.js/React application in development mode...")
process = subprocess.Popen(["npm", "start"], cwd="/var/jenkins_home/workspace/simple-node-js-react-app", stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)

# Wait for a moment to ensure the application is up and running
time.sleep(1)

# Write the process ID (PID) to a file
with open(".pidfile", "w") as pidfile:
    pidfile.write(str(process.pid))

print("The Node.js/React application is running. You can visit http://localhost:5000 to see it in action.")
