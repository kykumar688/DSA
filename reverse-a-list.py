import math
def getSizeInput():
    try:
        sizeofarray = int(input("Enter size N : "))  
    except ValueError:
        print("only expected number between 1 and 100")  
    if sizeofarray in range(1,10000):
        return sizeofarray
    else:
        print("wrong input!")
        exit() 


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



def reverseAnArray(arr):
    reversedarray = arr[::-1]  
    return reversedarray


def main():
    sizeofarray = getSizeInput()
    arr = getArrayInput()
    reversedarray = reverseAnArray(arr)
    for i in reversedarray:
        print(i, end = " ")

main()