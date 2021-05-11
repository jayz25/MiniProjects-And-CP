#from INPUTFILE import *
'''def primeKPFNums(A,B,K):
    prime = [True]*(B+1)
    prime_factors = [0] * (B+1)
    for p in range(2,B+1):
        if (prime_factors[p]==0):
            for i in range(p,B+1,p):
                prime_factors[i] = prime_factors[i] + 1
    for i in range(A,B+1):
        if (prime_factors[i]==K):
            print(i, end=" ")'''
try:
    arr = [0 for i in range(100001)]
    for i in range(2,100001):
        if arr[i]==0:
            for j in range(i,100001,i):
                arr[j]+=1 
    for i in range(2,100001):
        if arr[i]==0:
            arr[i]=1
    dp=[[0 for i in range(100001)]for _ in range(6)]
    for i in range(1,6):
        for j in range(2,100001):
            if arr[j]==i:
                dp[i][j]=1+dp[i][j-1]
            else:
                dp[i][j]=dp[i][j-1]
    for _ in range(int(input())):
        A,B,K = map(int,input().split())
        print(dp[K][B]-dp[K][A-1])
except EOFError as e: pass
