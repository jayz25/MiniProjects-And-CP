from collections import Counter

n, k = map(int, input().split())
k = min(k, 1007)

l = list(map(int, input().split()))

cnt = Counter(l)
print(cnt)

l = list(set(l))
print(l)
n = len(l)

mod = 10**9 + 7

dp = [[0 for _ in range(k+1)] for _ in range(n)]
print('1st dp',dp)

dp[0][0] = 1
dp[0][1] = cnt[l[0]]
print(dp)

for i in range(1, n):
    dp[i][0] = 1
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j] +cnt[l[i]]*dp[i-1][j-1]
        dp[i][j]%=mod
print('2nd dp' ,dp)

print(sum(dp[n-1][j] for j in range(k+1))%mod)
