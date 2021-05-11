'''
1 3 5 6
3 6 10
'''

T = int(input())
while T!=0:
    N,M = map(int,input().split())
    n = list(map(int,input().split()))
    m = list(map(int,input().split()))
    res = [0]
    V = 0
    res1 = []
    res2 = []
    res.extend(n) # OR operations value must be there since any OR 0 is ANYTHING L
    for i in range(N):
        for j in range(1,M):
            V = i or j
            res1.append(V)
    for i in range(N):
        for j in range(1,M):
            V = i and j
            res2.append(V)
    for i in range(len(res1)):
        fpr j in range(len(res2)):
            V = i or j


    T-=1
