arr = list(map(int,input().split()))
a = arr[0]
b = arr[1]
for i in range(a):
    input_list = list(map(int,input().split()))
    result = 0
    for j in range(b):
        result += input_list[j]
    print(result)