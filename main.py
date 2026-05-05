import os
import sys

# Move the working directory into the actual code folder
runtime_dir = os.path.join(os.path.dirname(__file__), "car_runtime")
os.chdir(runtime_dir)

# Add it to the Python path so imports work
sys.path.insert(0, runtime_dir)

# Run the real main.py
if __name__ == "__main__":
    with open("main.py", "r") as f:
        code = f.read()
    exec(code)
