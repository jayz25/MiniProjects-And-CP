
n=int(input("enter the length:"))
arr = list(map(int, input().split()))
    
print(arr)

def second():
    print("For every 3rd number,add 3")
    for i in range(1,n):
        if i % 3==0:
            print(arr[i]+3, end=' ')
    print()

def third():
    print("For every 5th number,sutract 7")
    for i in range(1,n):
        if i % 5==0:
            print(arr[i]-7, end=' ')
    print()

def fourth():
    sum=0
    print("print sum of number between 3 to 7")
    for i in range(3,8):
        sum=sum + arr[i]
    print()
    print(sum)

def rev():
    arr.reverse()
    print(arr)

second()
third()
fourth()
rev()