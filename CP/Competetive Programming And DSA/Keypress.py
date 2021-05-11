n = int(input())
pos = int(input())
s = list(str(input()))
d = {'PS':'S','SP':'S','RS':'R','SR':'R','PR':'P','RP':'P'}
for i in range(len(s)-2,-1,-1):

    print(s[i:i+2])
    print(d[str(s[i]+s[i+1])])
    s[i] = 'Z'
print(s)
