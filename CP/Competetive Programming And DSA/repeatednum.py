arr = [0,4,3,2,7,8,2,3,1]
size = len(arr)
count = 0
for i in range(size):
    x = arr[i] % size
    arr[x] = arr[x] + size
for i in range(size):
    if(arr[i]>= (size*2)):
        print(i, end=' ')
        count+=1
print()
print(count)