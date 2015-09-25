lst = str(input())
lst.split(" ")
S = 0
k = 0
for i in lst.split(" "):
    k += 1
    S += int(i)
print(S/k)