def euclid(n, m):
    if n >= m:
        if n % m == 0:
            return m
        else:
            return euclid(m, n % m)
    else:
        if m % n == 0:
            return n
        else:
            return euclid(n, m % n)


def rpfilter(a, *args):
    Smpl = list()
    for arg in args:
        if euclid(a, arg) == 1:
            Smpl.append(arg)
    return(Smpl)

a, *args = (int(i) for i in input().split())

if rpfilter(a, *args) == list():
    print(None)
else:
    for i in rpfilter(a, *args):
        print (i, end=' ')
