a = 'aaaba'
b = 'ababa'
c = 'aaaca'
h = 3
w = 5
res = a+b+c
dp = [[None for j in range(w)]for i in range(h)]
for i in range(h):
    for j in range(w):
        dp[i][j] = res[i+j]
print(dp)