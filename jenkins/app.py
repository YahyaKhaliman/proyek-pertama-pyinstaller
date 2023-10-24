import subprocess
import os

subprocess.run(["python", "-m", "compileall", "sources/"])
os.makedirs("build", exist_ok=True)

subprocess.Popen(["python", "app.py"])

print("Now...")
print("Visit http://localhost:5000 to see your Python application in action.")
