A = str(input())
n = int(input())
if A == "����":
    if n>=0:
          a=n%10
          if a == 0 or 5<=a<=9 or n%100==11 or n%100==12 or n%100==13 or n%100==14:
            print (n, "������")
          elif a == 1:
            print (n, "����") 
          elif (2<=a<=4 and n%100!=12) or (2<=a<=4 and n%100!=13) or (2<=a<=4 and n%100!=14):
            print (n, "�����")
if A == "�����":
    if n>=0:
          a=n%10
          if a == 0 or 5<=a<=9 or n%100==11 or n%100==12 or n%100==13 or n%100==14:
            print (n, "�����")
          elif a == 1:
            print (n, "�����") 
          elif (2<=a<=4 and n%100!=12) or (2<=a<=4 and n%100!=13) or (2<=a<=4 and n%100!=14):
            print (n, "�����")