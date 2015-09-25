A = str(input())
A.split(" ")
k = 0
chet = list()
nechet = list()
for i in A.split(" "):
    k += 1
    if k == 1:
        nechet.append (int(i))
    elif k%2 == 0:
        chet.append (int(i))
    elif k%2 == 1:
        nechet.append (int(i))
chet.sort(reverse=True)
nechet.sort()

itog = '*'
k = 0;
cht = 0;
ncht = 0;
for i in range (0, len(chet+nechet)):
    k += 1
    if k == 1:
        itog = itog + str(nechet[0]) + ' '
        ncht +=1;
    elif k%2 == 0:
        itog = itog + str(chet[cht]) + ' '
        cht +=1;
    elif k%2 == 1:
        itog = itog + str(nechet[ncht]) + ' '
        ncht +=1;

print(itog[1:len(itog)])