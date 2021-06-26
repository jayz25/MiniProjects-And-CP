def solve(arr,arr1,arr2,N,s1,s2,k):
    if N==0 or s1<0 or s2<0:
        return k
    if arr[N-1]<=s2 and arr1[N-1]<=s1:
        return max(solve(arr,arr1,arr2,N-1,s1-arr1[N-1],s2-arr[N-1],k+arr2[N-1]),solve(arr,arr1,arr2,N-1,s1,s2,k))
    else:
        return solve(arr,arr1,arr2,N-1,s1,s2,k)


arr = [50,40,30,20,10]  #Volumes
arr1 = [1,2,3,9,5]  #Masses 
arr2 = [300,480,270,200,180]  #Energies
s1 = 15 #Critical Mass
s2 = 100 #Capacity
N = 5
print(solve(arr,arr1,arr2,N,s1,s2,0))