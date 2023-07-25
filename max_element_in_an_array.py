import math
def getSizeInput():
    try:
        sizeofarray = int(input("Enter size N : "))  
    except ValueError:
        print("only expected number between 1 and 100")  
    if sizeofarray in range(1,100):
        return sizeofarray
    else:
        print("wrong input!")
        exit() 


def getArrayInput():
    try:
        arr = list(map(int,input("\nEnter the Numbers : ").split()))
    except:
        print("only expected numbers as input")
    return arr


def maxNum(sizeofarray,arr):
    maxnum = 0
    for i in range(0,sizeofarray):
        maxnum = max(arr)
    return maxnum


def main():
    sizeofarray = getSizeInput()
    arr = getArrayInput()
    maxnum = maxNum(sizeofarray,arr)
    print(maxnum)

main()