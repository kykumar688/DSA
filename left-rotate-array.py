import math

n,d=map(int,input("Enter the Numbers n,d : ").split())

def getArrayInput():
    try:
        arr = list(map(int,input("\nEnter the Numbers : ").split()))
    except:
        print("only expected numbers as input")
    for i in arr:
        if i >=1 and i <= 10000:
            return arr
    else:
        print("wrong input!")
        exit() 


def rotateList(d,arr):
    arr = arr[d:] + arr[:d]
    return arr


def main():
    arr = getArrayInput()
    rotatedarray = rotateList(d,arr)
    for i in rotatedarray:
        print(i, end = " ")

main()
