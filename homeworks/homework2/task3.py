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
        
N = input().split()
n = int(N[0])
m = int(N[1])
print(euclid(n, m))