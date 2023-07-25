

def twoPower(n):
    if (n&(n-1) == 0) and n!=0:
        print('True')
    else:
        print('False')
        

t = int(input("t :"))
for i in range(t):
    n = int(input("n :"))
    twoPower(n)