'''
2 3
2 2
2 2     n(your friend :) )
5 5 5   m(dumbfuck :D)
1 3 2 4   10   21
8 7 6
'''
try:
    T = int(input())
    def func(n,m):
        n.sort()
        m.sort(reverse=True)
        for i in range(1,len(n)+1):
            k = sum(n) - sum(n[:i]) + sum(m[:i])
            v = sum(m) - sum(m[:i]) + sum(n[:i])
            if k>v:
                return i
        return -1
    while T!=0:
        N, M = map(int,input().split())
        n = list(map(int,input().split()))
        m = list(map(int,input().split()))
        if n==m:
            print(-1)
        elif sum(n)>sum(m):
            print(0)
        else:
            print(func(n,m))
        T-=1
        
except EOFError as e: pass
        


        

        





























'''summ1 = sum(n)
        summ2 = sum(m)
        print(summ1,summ2)
        k = max(m)-min(n)
        l=0
        while True:
            if l>=N or l>=M:
                return -1
            if (summ1+k) > (summ2-k):
                l+=1
                return l
            else:
                n.remove(min(n))
                m.remove(max(m))
                k+= (max(m) - min(n))
                l+=1'''