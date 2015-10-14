def plural(n, L):
    if n >= 0:
          a = n % 10
          if a == 0 or 5 <= a <= 9 or n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
            return (L[2])
          elif a == 1:
            return (L[0])
          elif (2 <= a <= 4 and n % 100 != 12) or (2 <= a <= 4 and n % 100 != 13) or (2 <= a <= 4 and n % 100 != 14):
            return (L[1])


A = input()
n = int(input())

L1 = ['утюг', 'утюга', 'утюгов']
L2 = ['гармошка', 'гармошки', 'гармошек']
L3 = ['ложка', 'ложки', 'ложек']
L4 = ['чайник', 'чайника', 'чайников']

if A == 'утюг':
    print(n, plural(n, L1))
elif A == 'гармошка':
    print(n, plural(n, L2))
elif A == 'ложка':
    print(n, plural(n, L3))
else:
    print(n, plural(n, L4))
