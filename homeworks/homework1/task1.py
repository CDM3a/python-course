A = str(input())
n = int(input())
if A == "утюг":
    if n>=0:
          a=n%10
          if a == 0 or 5<=a<=9 or n%100==11 or n%100==12 or n%100==13 or n%100==14:
            print (n, "утюгов")
          elif a == 1:
            print (n, "утюг") 
          elif (2<=a<=4 and n%100!=12) or (2<=a<=4 and n%100!=13) or (2<=a<=4 and n%100!=14):
            print (n, "утюга")
if A == "ложка":
    if n>=0:
          a=n%10
          if a == 0 or 5<=a<=9 or n%100==11 or n%100==12 or n%100==13 or n%100==14:
            print (n, "ложек")
          elif a == 1:
            print (n, "ложка") 
          elif (2<=a<=4 and n%100!=12) or (2<=a<=4 and n%100!=13) or (2<=a<=4 and n%100!=14):
            print (n, "ложки")