import re
import sys


data = sys.stdin.read()
code_lines = data.split("\n")

for i in range(len(code_lines)):
    ids = re.findall("\w+" + " = " + ".+", code_lines[i])
    if ids:
        A = re.findall("^\w+", ids[0])
        print(i+1, A[0])
