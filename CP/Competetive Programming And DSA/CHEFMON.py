try:
    for _ in range(int(input())):
        N, B = map(int,input().split())
        arr = list(map(int,input().split()))
        res = []
        start = 0
        end = 0
        while(end<N):
            k = sum(arr[start:end])
            if k==B:
                print(k)
                break
            elif k<=B:
                res.append(k)    
            if k>B:
                start+=1
            else:
                i+=1
            if start==end and sum(arr[start:end])>B:
                start+=1
                end+=1
        print(max(res))

            

except EOFError as e:
    pass        
        