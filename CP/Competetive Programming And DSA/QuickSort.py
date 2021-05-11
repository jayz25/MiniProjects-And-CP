#Create Array
# Code Refrenced from https://www.sanfoundry.com/python-program-implement-quicksort/
#Select Pivot?? Divinde array around Pivot lesser than/greater than return do the same with 2 halves
def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = end - 1

    while True:
        while(i<=j and arr[i]<=pivot):
            i = i + 1
        while(i<=j and arr[j]>=pivot):
            j = j - 1
        
        if i <= j:
            arr[i], arr[j] = arr[j],arr[i]
        else:
            arr[low],arr[j] = arr[j],arr[low]
            return j 
def quickSort(arr,low,high):
    if high - low > 1:
        p = partition(arr,low,high)
        quickSort(arr,low,p)
        quickSort(arr,p+1,high)

if __name__ == '__main__':
    arr = input('Enter The List Of The Numbers: ').split()
    arr = [int(x) for x in arr]
    quickSort(arr,0,len(arr))
    print('Sorted list: ', end=' ')
    print(arr)
