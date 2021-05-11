n=int(input("enter the length:"))
arr = list(map(int, input().split()))
sum = 0
for i in arr[n::-1]:
    print(i, end=' ')
print()

for i in arr[::3]:
    if arr.index(i)!=0:
        print(i+3, end=' ')
print()
for i in arr[::5]:
    if arr.index(i)!=0:
        print(i-7, end=' ')
print()
for i in arr[3:8]:
    sum=sum+i
print(sum)
