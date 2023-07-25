

def binaryRep(n):
    n = bin(n)[2:]
    print(n)
        

t = int(input("t :"))
for i in range(t):
    n = int(input("n :"))
    binaryRep(n)