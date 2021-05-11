'''S1 = "AGGTAB"
m = len(S1)
S2 = "GXTXAYB"
n = len(S2)
t = [[0 for i in range(n+1)]for j in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            t[i][j] = 0
        elif S1[i-1]==S2[j-1]:
            t[i][j] = 1 + t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
print(t[m][n])
res = ""
i = m
j = n
while i>0 and j>0:
    if S1[i-1] == S2[j-1]:
        res+=S1[i-1]
        i-=1
        j-=1
        
    elif t[i-1][j] > t[i][j-1]:
        i-=1
    else:
        j-=1
print(res[::-1])'''
A = "great" 
n = len(A)
print(A[:2])
print(A[0:2])
print(A[:-2])
print(A[-2:])
print(A[2:n])
print(A[2:n-2])