#CODECHEF MAXFUN FEBRUARY LONG CHALLENGE
from itertools import combinations
try:
    def sumtriplet(a,b,c):
        return abs(a-b)+abs(a-c)+abs(b-c)
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int,input().split()))
        #res = []
        #comb = list(combinations(arr,3))
        #print(comb)
        mx = max(arr)
        mn = min(arr)
        m = -1
        for i in range(N):
            m = max(m,sumtriplet(arr[i],mx,mn))
        print(m)        

            
except EOFError as e:
    pass
