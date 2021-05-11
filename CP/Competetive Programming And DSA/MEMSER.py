try:
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(str,input().split()))
        res = 0
        k = 0
        for i in arr:
            if (i=='start' or i=='restart') and k==0:
                k=1
                res = 200
            elif (i=='stop') and k==1:
                k=0
                res = 200
            elif (i=='stop') and k==0:
                res = 404
        print(res)
except EOFError as e:
    pass
            