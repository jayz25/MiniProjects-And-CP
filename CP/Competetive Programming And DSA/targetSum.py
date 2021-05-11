def subsetSum(arr,_sum,n):
    if _sum==0:
        return True
    if n==0:
        return False
    if arr[n-1] > _sum:
        return subsetSum(arr,n-1,_sum)
    return subsetSum(arr,_sum-arr[n-1],n-1) or subsetSum(arr,_sum,n-1)
arr = [3,2,9,2]
n = len(arr)
#temp = [[None for i in range(n+1)]for j in range(n+1)]

target = 9
print(subsetSum(arr,target,n))
#subsetSumMemoization(temp,arr,0,n-1,target)
#print(temp)
#print(temp[n][n])