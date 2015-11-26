import re
import sys


data = sys.stdin.read()
numbers = data.split("\n")
del numbers[-1]

for i in range(len(numbers)):
    for k in range(0,9):
        A = str(k) + "{3}"
        nice_num = re.findall(A, numbers[i])
        if nice_num:
            print(numbers[i])
