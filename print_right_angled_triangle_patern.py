import math
def getTInput():
    try:
        t = int(input("enter T: "))  
    except ValueError:
        print("only expected number between 1 and 100")  
    if t in range(1,101):
        return t
    else:
        print("wrong input!")
        exit() 
        
def getNInput():
    try:
        n = int(input("enter N: "))  
    except ValueError:
        print("only expected number between 1 and 100")  
    if n in range(1,101):
        return n
    else:
        print("wrong input!")
        exit()

def rightTriangle(n):
    for i in range(n+1):
        for j in range (1,n-i+1):
            print(" ",end="")
        for j in range (n-i+1,n+1):
            print("*",end="")
        print()


def main():
    t = getTInput()
    for i in range(t):
        print("case #"+ str(i+1) + ":", end="")
        n = getNInput()
        rightTriangle(n)
    
main()