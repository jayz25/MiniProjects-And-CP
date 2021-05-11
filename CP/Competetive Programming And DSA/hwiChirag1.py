def isTriangle(a,b,c):
    if (a+b>=c) or (b+c>=a) or (c+a>=b):
        return True
    else:
        return False
N = int(input())
arr = []
setS = set()
for i in range(N):
    arr.appned(int(input()))
for i in range(1,N-2):
    if isTriangle(arr[i-1],arr[i],arr[i+1]):
        setS.add(arr[i-1])
        setS.add(arr[i])
        setS.add(arr[i+1])
return len(setS)

