for i in range(int(input())):
    n = int(input())
    dp = [0 for x in range(n)]
    ls = [int(x) for x in input().split()]
    dp[0] = 1
    for k in range(n-1):
        if dp[i+1]>=dp[i]:
            dp[i+1] = 1+dp[i]
        else:
            dp[i+1]=1
    print(sum(dp))
