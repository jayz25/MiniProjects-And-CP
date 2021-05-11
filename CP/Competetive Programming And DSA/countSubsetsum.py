arr = [2,3,5,6,8,10]
s = 10
n = len(arr)
t = [[None for i in range(s+1)]for j in range(n+1)]
t[0][0]=1
for i in range(1,n+1):
    t[i][0]=1
for i in range(1,s+1):
    t[0][i]=0
for i in range(1,n+1):
    for j in range(1,s+1):
        if arr[i-1]<=j:
            t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
        else:
            t[i][j]=t[i-1][j]
print(t[n][s])