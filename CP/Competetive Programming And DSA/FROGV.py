N, K, P = map(int,input().split())
arr = list(map(int,input().split()))
table = [[0 for i in range(n)]for i in range(n)]
ls = arr
arr.sort()
for i in range(n):
    for j in range(n):
        if abs(ar