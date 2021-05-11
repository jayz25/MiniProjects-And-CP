#Anticlockwise  = ['Ru','Lu','Ld','Rd']
#Clock = ['Ru','Rd','Ld','Lu']
import sys

'''
2
5 5 4 4
5 2 3 1
5 5
3 5'''
def getInput(): return sys.stdin.readline().strip()
def getInt(): return int(input())
def getInts(): return map(int,input().split())
def getArray(): return list(getInts())

t = getInt()
for _ in range(t):
    n, k, x, y = getInts()
    if x==y:
        print(n,n)
    else:
        
        if x<y:
            first = (x+n-y,n)
            second = (n,x+n-y)
            third = (y-x,0)
            fourth = (0,y-x)
        else:
            first = (n,y+n-x)
            second = (y+n-x,n)
            third = (0,x-y)
            fourth = (x-y,0)
        dic = {1:first,2:second,3:third,4:fourth}
        effective_collision = ((k-1)%4) + 1
        print(*dic[effective_collision])