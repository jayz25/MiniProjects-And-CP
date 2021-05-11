def findpeakutil(arr,low,high,n):
    mid = low + (high-low)//2

    if(mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
        return mid
    if(mid>0 and arr[mid]>=arr[mid-1]):
        return findpeakutil(arr,low,mid-1,n)
    else:
        return findpeakutil(arr,mid+1,high,n)
def findpeak(arr,n):
    return findpeakutil(arr,0,n-1,n)
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print(findpeak(arr,n))
