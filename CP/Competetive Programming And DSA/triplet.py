def countTriplets(arr,n,m):
    count = 0
    arr.sort()
    for end in range(n-1,1,-1):
        start = 0
        mid = end -1
        while(start<mid):
            prod = (arr[end] * arr[start] * arr[mid])
            if prod>m:
                mid=-1
            elif prod<m:
                start+=1
            elif prod==m:
                count+=1
                mid-=1
                start+=1
    return count


arr = [1,4,6,2,3,8]
# 1,2,3,4,6,8
m = 24
n = len(arr)
print(countTriplets(arr,n,m))