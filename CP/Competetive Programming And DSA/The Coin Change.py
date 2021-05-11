n, m = input().split()
c = list(map(int, input().split()))
def coin(c,n):
    table = [0 for i in range(n+1)]

    table[0] = 1

    for i in range(0,l):
        for j in range(c[i],n+1):
            table[j] += table[j-S[i]]
    return table[n]

