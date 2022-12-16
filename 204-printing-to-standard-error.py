# script_1.py
print("printing...")

$ python script_1.py 1>out.txt 2>err.txt

$ wc -l out.txt err.txt
    1 out.txt
    0 err.txt
    1 total

# script_2.py
import sys
print("printing...", file=sys.stderr)

$ python script_2.py 1>out.txt 2>err.txt

$ wc -l out.txt err.txt
    0 out.txt
    1 err.txt
    1 total