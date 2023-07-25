import math

X,Y=map(float,input("Enter X Y: ").split())

def withdrawAmount(X):
    try:
        X = int(X)
    except ValueError:
        print("only expected number between 1 and 100")  
    if X in range(1,2001):
        return X    
    else:
        print("wrong input!")
        exit()

def accountBalance(Y):
    try:
        Y = float(Y)
    except ValueError:
        print("only expected number between 1 and 100")  
    if Y in range(1,2001):
        return Y    
    else:
        print("wrong input!")
        exit()


def cashWithdraw():
    a = withdrawAmount(X)
    b = accountBalance(Y)
    if a+0.5 <= b and a % 5 == 0:
        balance = float(b-a-0.50)
    else:
        balance = b
    return balance
    
def main():
    balance = cashWithdraw()
    print(balance)

main()
