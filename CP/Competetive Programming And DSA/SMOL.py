#FEBRUARY LUNCHTIME 2021
try:
    for _ in range(int(input())):
        N,K = map(int,input().split())
        if K==0:
            print(K)
        else:
            print(N%K)
except EOFError as e:
    pass