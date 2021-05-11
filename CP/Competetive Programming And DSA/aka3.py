t = int(input())
sq = []
a1 = int(input())
d = int(input())
n = int(input())
ans = a1
for i in range(n):
    print(ans,end=' ')
    sq.append(ans)
    ans+=d
print()
sum = 0
for i in range(n):
    sq[i]*=sq[i]
    sum+=sq[i]
for i in range(n):
    print(sq[i], end=' ')
print()
print(sum)
