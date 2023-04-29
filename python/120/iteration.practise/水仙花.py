
for n in range(100,1000):
    n=str(n)
    n1,n2,n3=int(n[0])**3,int(n[1])**3,int(n[2])**3
    if  n1+n2+n3==int(n):
        print(n)