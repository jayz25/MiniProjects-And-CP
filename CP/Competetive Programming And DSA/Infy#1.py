def solve(arr,i,n,type):
    if i==n:
        return 0
    
    for type in arrSet:
        if arr[i]==type:
            dp[type] = 1 + solve(arr,i+2,n,type)
        else:
            dp[type] = solve(arr,i+1,n,type)
    


arr = list(map(int,input().split()))
arrSet = set(arr)

while(i<n):
    if arr[i]!=
