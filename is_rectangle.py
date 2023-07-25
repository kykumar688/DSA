import math

def getSideInput():
    try:
        A = int(input("Enter size A : "))
        B = int(input("Enter size B : "))
        C = int(input("Enter size C : "))
        D = int(input("Enter size D : "))
        arr = [A,B,C,D]
    except ValueError:
        print("only expected number between 1 and 100")  
    if A in range(1,10000) and B in range(1,10000) and C in range(1,10000) and D in range(1,10000):
        return arr
    else:
        print("wrong input!")
        exit()
    

def isRectangle(arr):
    side = []
    cnt = 0
    for i in arr:
        k = arr.count(i)    
        if k == 2:
            side.append(i)
    side = set(side)
    if len(side) == 2:
        return 1
    else:
        return 0



def main():
    arr = getSideInput()
    isrect = isRectangle(arr)
    print(isrect)

main()
