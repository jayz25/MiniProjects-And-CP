n = int(input())
s = list(str(input()))
e = s[0]
cnt=1
for i in range(1,n):
    if s[i]!=e:
        cnt+=1
        e = s[i]
print(cnt)