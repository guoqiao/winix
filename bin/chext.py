import os
import sys

# Set the directory containing the files
directory = "."  # Change this to your directory

# Loop through all files in the directory
for filename in os.listdir('.'):
    # Check if the file has a .bat extension
    if filename.lower().endswith(".bat"):
        # Construct the new filename with a .cmd extension
        new_filename = os.path.splitext(filename)[0] + ".cmd"
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed {filename} to {new_filename}")
