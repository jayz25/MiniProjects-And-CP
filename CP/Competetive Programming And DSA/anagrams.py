def anagram2(a,b):
    count=0
    if len(a)!=len(b):
        return "NO"
    for i in range(len(a)):
        count+=ord(a[i])
        print(count)
    for i in range(len(b)):
        count-=ord(b[i])
        print(count)
    if count==0:
        return "YES"
    else:
        return "NO"
def anagram(a,b):
    if len(a)!=len(b):
        return "NO"
    a = sorted(a)
    b = sorted(b)
    if a==b:
        return "YES"
    else:
        return "NO"
a, b = map(str,input().split())
print(anagram2(a,b))

