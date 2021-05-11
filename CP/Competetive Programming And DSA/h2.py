A = input()
N,K = map(int,A.split())
arr = list(map(int,input().split()))
res = set()
for i in arr:
    if i+K in arr:
        res.add(i)
        res.add(i+K)
print(N,K)
print(arr)
print(res)

