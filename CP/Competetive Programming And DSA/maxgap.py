def solve(arr,i,j):
    if arr[i]>=arr[j]:
        return j-i
    else:
        return max(solve(arr,i+1,j),solve(arr,i,j-1))


n = int(input())
arr = list(map(int,input().split()))
print(solve(arr,0,n-1))