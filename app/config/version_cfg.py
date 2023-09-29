# Import VERSION from the parent directory
import os
import sys

# Determine the path to the parent directory (the directory containing app)
parent_dir = os.path.dirname(os.path.abspath(__file__))
#print(parent_dir)
version_file = os.path.join(parent_dir, "..\..", "VERSION")

# Check if the VERSION file exists
if os.path.exists(version_file):
    # Open and read the VERSION file
    #print("VERSION file exists.")
    with open(version_file, "r") as f:
        VERSION = f.read().strip()
else:
    # Provide a default value if the VERSION file doesn't exist
    VERSION = "0.0.0"
