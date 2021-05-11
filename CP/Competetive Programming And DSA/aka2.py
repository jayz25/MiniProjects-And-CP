t = int(input())
while(t!=0):
    x1 = int(input())
    x2 = int(input())
    y1 = int(input())
    y2 = int(input())
    first = (x2-x1)*(x2-x1)
    second = (y2-y1)*(y2-y1)
    ans = (first+second)**2
    print(ans)
