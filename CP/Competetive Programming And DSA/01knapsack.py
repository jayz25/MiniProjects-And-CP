#Recursive With Memoization
def knap(arr,wt,W,n):
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]
    if wt[n-1]<=W:
        t[n][W] = max(arr[n-1]+knap(arr,wt,W-wt[n-1],n-1),knap(arr,wt,W,n-1))
        return t[n][W]
    else:
        t[n][W] = knap(arr,wt,W,n-1)
        return t[n][W]
#Recursive Approach
def knapsack(arr,wt,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(arr[n-1]+knapsack(arr,wt,W-wt[n-1],n-1),
        knapsack(arr,wt,W,n-1))
    else:
        return knapsack(arr,wt,W,n-1)
arr = list(map(int,input().split()))
wt = list(map(int,input().split()))
W = int(input())
n = len(arr)
t = [[-1 for i in range(W+1)]for i in range(n+1)]
for i in range(n+1):
    t[i][0]=0
for j in range(W+1):
    t[0][j]=0
for i in range(1,n+1):
    for j in range(1,W+1):
        if wt[i-1]<=j:
            t[i][j] = max(arr[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
print(t[n][W])

#print(knapsack(arr,wt,W,n))        
#print(knap(arr,wt,W,n))
