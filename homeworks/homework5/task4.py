import re
import sys


data = sys.stdin.read()
code_lines = data.split("\n")

for i in range(len(code_lines)):
    ids = re.findall(".+ = ", code_lines[i].strip())
    if ids and ids[0][0] != "#":
        var_list = ""
        vars = re.findall(" *([\w,. ]+) = ", ids[0])
        if vars:
            vars_m = vars[0].split(",")
            for k in range(len(vars_m)):
                var_list += vars_m[k]
            print(i+1, var_list)

