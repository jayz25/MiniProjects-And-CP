from sys import stdin
input = lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
from bisect import bisect_left
def beauty(n,m,s,x,y):
    degree=[0 for i in range(n)]
    graph={i:[] for i in range(n)}
    for i in range(m):
        x[i]-=1
        y[i]-=1
        graph[x[i]].append(y[i])
        degree[y[i]]+=1
    q=deque()
    for i in range(n):
        if degree[i]==0:
            q.append(i)
        count=0
        ans=0
        dp=[[0 for i in range(26)]for i in range(n)]
    while count<n and q:
        a=q.popleft()
        count+=1
        dp[a][ord(s[a])-97]+=1
        for i in graph[a]:
            for j in range(26):
                dp[i][j]=max(dp[i][j],dp[a][j])
            degree[i]-=1
            if degree[i]==0:
                q.append(i)
    if count!=n:
        return -1
    else:
        ans=0
        for i in range(n):
            ans=max(ans,max(dp[i]))
        return ans
print(beauty(6,6,"xzyabc",[1,3,2,5,4,6],[2,1,3,4,3,4]))
print(beauty(5,4,"abaca",[1,1,3,4],[2,3,4,5]))