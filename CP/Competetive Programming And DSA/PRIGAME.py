try:
    K = 1000007
    count_prime = [None]*(K+1)
    sieve = [True]*(K+1)
    i = 2
    while(i*i<=K):
        if sieve[i]:
            for j in range(i*i,K+1,i):
                sieve[j] = False
        i+=1

    count_prime[0] = 0
    count_prime[1] = 0
    for i in range(2,K+1):
        count_prime[i] = count_prime[i-1]
        if sieve[i]:
            count_prime[i]+=1
    for _ in range(int(input())):
        x, y = map(int,input().split())
        res = count_prime[x]
        if res>y:
            print("Divyam")
        else:
            print("Chef")
except EOFError as e:
    pass