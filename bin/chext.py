import os
import sys

args = sys.argv
assert len(sys.argv) >= 2

def fmt(ext):
    """Ensure ext format in lower case and starts with ., ex: .bat"""
    return '.' + ext.strip().strip('.').lower()

from_ext = fmt(args[0])
to_ext = fmt(args[1])

if len(args) == 3:
    root = args[2]
else:
    root = '.'


total = 0
# Loop through all files in the directory
for filename in os.listdir(root):
    # Check if the file has a expected extension
    if filename.lower().endswith(from_ext):
        # Construct the new filename with a .cmd extension
        new_filename = os.path.splitext(filename)[0] + to_ext
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed {filename} to {new_filename}")
        total += 1
print(f'total renamed: {total}')
