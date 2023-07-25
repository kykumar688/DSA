
def getArray1Input():
    try:
        arr1 = list(map(int,input("\nEnter the Numbers : ").split()))
    except:
        print("only expected numbers as input")
    for i in arr1:
        if i >=1 and i <= 10000:
            return arr1
    else:
        print("wrong input!")
        exit() 

def getArray2Input():
    try:
        arr2 = list(map(int,input("\nEnter the Numbers : ").split()))
    except:
        print("only expected numbers as input")
    for i in arr2:
        if i >=1 and i <= 10000:
            return arr2
    else:
        print("wrong input!")
        exit() 

def compare(arr1,arr2):
    a = 0
    b = 0
    
    for i in range(0,3):
        if arr1[i] > arr2[i]:
            a = a+1
        if arr1[i] < arr2[i]:
            b = b+1
    
    arr3 = [a,b]
    return arr3

def main():
    arr1 = getArray1Input()
    arr2 = getArray2Input()
    score =  compare(arr1,arr2)
    for i in score:
        print(i, end = " ")
      

main()