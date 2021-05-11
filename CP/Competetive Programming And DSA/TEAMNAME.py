
try:
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(str,input().split()))
        pre = set()
        res = {}
        for i in arr:
            pre.add(i[0])
            if i[1:] in res:
                res[i[1:]]+=1
            else:
                res[i[1:]] = 1
        print(pre)
        print(res)
        for i in pre:
            for j in res:
                if str(i+j)     
except EOFError as e:
    pass
    
            