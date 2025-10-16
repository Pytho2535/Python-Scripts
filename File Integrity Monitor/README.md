# File Integrity Monitor
<b>REMEMBER TO CHANGE PATH INSIDE</b>
## Description
Reads a list of file paths from files.txt
Calculates SHA-256 hashes for each file
Creates and stores a trusted baseline (baseline.json)
Compares current hashes with the baseline

Detects:
- Modified files
- Unchanged files
- New files
