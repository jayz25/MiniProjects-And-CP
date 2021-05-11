'''
2
8 38
7 8 19 7 8 7 10 20
4 5
2 10 4 9

7
2
'''

def some(N,K,l):
    if sum(l)<=(2*K):
        return -1
    S = K
    res = []
    for i in range(N):
        if l[i]<=S:
            S = S - l[i]
            count+=1
            res.append(i)
        if S<=0:
            break
    for i in res:
        del l[i]
    for i in range(1,len(l)+1):
        if sum[:i]>=K:
            count+=i
            return count
    return -1
    

        
        
def co(N,K,l):
    K=K*2
    subs = ([[0 for i in range(K+1)]for i in range(N+1)])
    
    for i in range(1,K+1):
        subs[0][i] = 10**9-1
    for i in range(1,N+1):
        for j in range(1,K+1):
            if l[i-1] > j:
                subs[i][j] = subs[i-1][j]
            else:
                subs[i][j] = min(subs[i-1][j],subs[i][j-l[i-1]]+1)
    return subs[N][K]
            
    
    




T = int(input())
while T!=0:
    N, K = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    print(co(N,K,l))
    T-=1
            
        
