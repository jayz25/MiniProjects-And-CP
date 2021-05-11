for i in range(int(input())):
    target = int(input())
    dp = [0 for x in range(target+1)]
    dp[0] = 1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    
    for k in range(4,target+1):
        dp[k] = dp[k-2] + dp[k-3]
    print(dp[target]%(10^9+9))
        