S1 = "AGGTAB"
S2 = "GXTXAYB"
m = len(S1)
n = len(S2)
#Finding LCS of S1 and S2 
#Then Printing Shortest Common SuperSequence by  Traversing back LCS array
t = [[0 for i in range(n+1)] for j in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            t[i][j] = 0
        elif S1[i-1]==S2[j-1]:
            t[i][j] = 1 + t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
i = m
j = n
res = ""
while i>0 and j>0:
    if S1[i-1]==S2[j-1]:
        res+=S1[i-1]
        i-=1
        j-=1
    else:
        if t[i][j-1] > t[i-1][j]:
            res+=S2[j-1]
            j-=1
        elif t[i-1][j] >= t[i][j-1]:
            res+=S1[i-1]
            i-=1
print(i,j)
if i>0:
    res+=S1[:i]
if j>0:
    res+=S2[:j]
print(res[::-1])