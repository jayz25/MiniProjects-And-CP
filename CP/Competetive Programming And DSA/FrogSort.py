try:
    import math
    for _ in range(int(input())):
        N = int(input())
        W = list(map(int,input().split()))
        L = list(map(int,input().split()))
        D = {}
        re = 0
        for i in range(1,N+1):
            D[i] = W.index(i)
            print(D)
        for i in range(2,N+1):
            t_uno = D[i]
            t_duo = D[i-1]
            t = 0
            print(t_uno,t_duo)
            if t_uno<t_duo:
                t = (math.ceil((t_duo+1-t_uno)/L[t_uno]))
            re+=t
            D[i]+=t*(L[t_uno])
        print(re)
except EOFError as e:
    pass