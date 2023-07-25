import math
def getSizeInput():
    try:
        sizeofarray = int(input())  
    except ValueError:
        print("only expected number between 1 and 100")  
    if sizeofarray in range(1,100):
        return sizeofarray
    else:
        print("wrong input!")
        exit() 


def getArrayInput():
    try:
        arr = list(map(int,input().split()))
    except:
        print("only expected numbers as input")
    for i in arr:
        if i >=1 and i <= 10000:
            return arr
    else:
        print("wrong input!")
        exit() 


def uniqueSet(arr):
    uniqueset = []
    for i in arr:
        k = arr.count(i)
        if k <= 1:
           uniqueset.append(i)  
    return uniqueset


def main():
    sizeofarray = getSizeInput()
    arr = getArrayInput()
    uniqueset = uniqueSet(arr)
    print(' '.join(uniqueset))

main()