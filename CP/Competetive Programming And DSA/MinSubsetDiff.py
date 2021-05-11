arr = list(map(int,input().split()))
n = len(arr)
e = sum(arr)
v = []
min_diff = 2**31
t = [[None for i in range(e+1)]for j in range(n+1)]
for i in range(n+1):
    t[i][0] = True
for i in range(1,e+1):
    t[0][i] = False
for i in range(1,n+1):
    for j in range(1,e+1):
        if arr[i-1]<=j:
            t[i][j] = t[i-1][j-arr[i-1]] | t[i-1][j]
        else:
            t[i][j] = t[i-1][j]

for i in range(int(e/2)+1):
    if t[n][i]==True:
        v.append(i)
for i in v:
    min_diff = min(min_diff,(e-2*i))
print(min_diff)



