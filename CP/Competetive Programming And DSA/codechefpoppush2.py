s = str(input())
arr = []
arr[:0] = s
print(arr)
res = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]!=arr[j]:
            res.append(j-i)
print(max(res))
        