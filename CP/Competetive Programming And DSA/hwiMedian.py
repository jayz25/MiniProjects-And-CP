def median(arr):
    i = 0
    j = len(arr)-1
    print(arr)
    if j==1:
        return arr[0]
    if i+j & 1:
            
        return (arr[((i+j)//2)] + arr[((i+j)//2) + 1])//2
    else:
        return arr[(i+j)//2]
    
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
X = int(input())
cnt = 0
for i in range(N):
    for j in range(i,N):
        if median(arr[i:j+1])==X:
            cnt+=1

            
print(cnt)
