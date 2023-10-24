import subprocess
import os

# Build the Python application (replace with actual build commands)
subprocess.run(["python", "-m", "compileall", "sources/"])
os.makedirs("build", exist_ok=True)

# Run the Python application in development mode
subprocess.Popen(["python", "app.py"])

print("Now...")
print("Visit http://localhost:3000 to see your Python application in action.")
