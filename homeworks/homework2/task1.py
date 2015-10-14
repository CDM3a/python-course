def prime(x):
    if x > 1:
        if x == 2:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    S = False 
                    break
                else:
                    S = True
            if S == False:
                return False
            else:
                return True
              
N = int(input())
for i in range(1, N+1):
    x = int(input())
    print (prime(x))
