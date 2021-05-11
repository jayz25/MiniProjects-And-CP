import math
#CODECHEF FEBRUARY LONG CHALLENGE
'''def immaretard(W,L):
    mx = max(W)
    mn = min(W)
    mx_wt = L[W.index(mx)]
    mn_wt = L[W.index(mn)]
    while(mn!=W[0]):
        W.insert(0+L[0],W[0])
        W.pop(W.index(W[0]))
    
    
        
    while(mx!=W[-1]):
        try:
            W[W.index(mx)]= W[W.index(mx)+mx_wt]
        except IndexError:
            W.pop(W.index(mx))
            W.append(mx)
'''
for _ in range(int(input())):
    N = int(input())
    W = list(map(int,input().split()))
    L = list(map(int,input().split()))
    res = [None,None,None,None]
    W.extend(res)
    
    print(W)
    count = 0
    i = 0
    while(i!=(N-1)):
        if W[i]>W[i+1]:
            if i+L[i]<N:
                    count = count + math.ceil(N/L[i])
                    W.append(W.pop(i))
                    L.append(L.pop(i))
            else:
                W.append(W.pop(i))
                L.append(L.pop(i))
                count+=1

            print(W)
            print("count = ",end='')
            print(count)
        else:
            i+=1

    print(count)

    
   
        