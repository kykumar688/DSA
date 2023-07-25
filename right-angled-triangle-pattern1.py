import math
def getSizeInput():
    try:
        n = int(input("enter N: "))  
    except ValueError:
        print("only expected number between 1 and 100")  
    if n in range(1,50):
        return n
    else:
        print("wrong input!")
        exit() 


def trianglePattern(n):
    a = 1
    for i in range(1,n+1):
        for j in range(i):
            print(a,end=" ")
            a = a+1
        print()



def main():
    n = getSizeInput()
    trianglePattern(n)

main()