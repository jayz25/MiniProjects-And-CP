N = int(input())
arr = list(map(int,input().split()))
days = 0
for i in range(N):
    if arr[i] < 2:
        pass
    else:
        quotient = arr[i]//2
        days+=quotient
print(days)
        

        