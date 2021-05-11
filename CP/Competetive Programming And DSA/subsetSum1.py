arr = list(map(int,input().split()))
e = int(input())
n = len(arr)
t=[[None for i in range(e+1)]for j in range(n+1)]
for i in range(n+1):
    t[i][0]=True
for j in range(1,e+1):
    t[0][j]=False
for i in range(1,n+1):
    for j in range(1,e+1):
        if j<arr[i-1]:
            t[i][j]=t[i-1][j]
        else:
            t[i][j]= (t[i-1][j] or t[i-1][j-arr[i-1]])

print(t[n][e])

