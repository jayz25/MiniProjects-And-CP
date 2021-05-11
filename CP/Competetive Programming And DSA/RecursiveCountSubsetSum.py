'''If you want to find the count the number of subsets
which have difference "diff"(given value) we can implement this code in
that, Suppose given an array [1,1,2,3] we are supposed to
find the number of subsets which have difference = 1
then..let's assume we need (S1-S2)=1
and S1+S2=sum(arr) (two subsets sum is total arr sum)
now    S1-S2=1
    +  S1+S2=sum(arr)
    =  2*S1 = (sum(arr)+1)
    =   S1 = (sum(arr)+1)/2
    i.e S1 = (sum(arr)+"given_difference)/2
    so count the number of subsets with given
    sum S1 and it will be eqal to the number
    of subsets which have given difference.'''
def subsetSum(arr,n,i,s,count):
    if i==n:
        if s==0:
            count+=1
        return count
    count = subsetSum(arr,n,i+1,s-arr[i],count)
    count = subsetSum(arr,n,i+1,s,count)
    return count


arr = [1,1,2,3]
n = len(arr)
s = 4

print(subsetSum(arr,n,0,s,0))

