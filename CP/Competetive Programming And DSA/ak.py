def findoptimal(N):
    if N<=6:
        return N
    maxi = 0
    for b in range(N-3,0,-1):
        curr = (N-b-1)*findoptimal(b)
        if curr > maxi:
            maxi = curr
    return maxi

if __name__=='__main__':
    k = int(input())
    print('Maximum Number Of A\'s', findoptimal(k))