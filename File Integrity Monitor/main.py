"""
This Python script calculates and tracks SHA-256 hashes of files to detect any unauthorized changes.
- Reads a list of file paths from `files.txt`
- Generates SHA-256 hashes for each file
- Creates a baseline of known-good hashes saved in `baseline.json`
- Compares current file hashes to the baseline to detect modifications, new, or missing files
- Prints the results to the console
"""

import hashlib
import json


def get_file_hash(file):
    hashes = {}
    with open(file, 'r') as f:
        file_path = [line.strip() for line in f.readlines()]
    
        for path in file_path:
            with open(path, 'rb') as f:
                data = f.read()
                m = hashlib.sha256()
                m.update(data)
                hashes[path] = m.hexdigest()
        return hashes
        
def create_baseline(hashes):
    with open('baseline.json', 'w') as f:
        json.dump(hashes, f, indent=4)
    print("[*] baseline.json created successfully.")

        
def check_integrity(file):
    current_hash = {}
    with open('baseline.json', 'r') as f:
        baseline = json.load(f)

    with open(file, 'r') as f:
        file_path = [line.strip() for line in f.readlines()]
    
        for path in file_path:
            with open(path, 'rb') as f:
                data = f.read()
                m = hashlib.sha256()
                m.update(data)
                current_hash[path] = m.hexdigest()
    for path, hash_value in current_hash.items():
        if path not in baseline:
            print(f"[NEW] {path} was not in baseline.")
        elif baseline[path] != hash_value:
            print(f"[CHANGED] {path} has been modified!")
        else:
            print(f"[OK] {path} is unchanged.")
    return current_hash



hash_data = get_file_hash(r'PATH') # CHANGE PATH



option = input("""Choose Option:
[1] Set new baseline
[2] Compare hashes to baseline
""")

if option == '1':
    create_baseline(hash_data)
elif option == '2':
    check_integrity(r'PATH') # CHANGE PATH
