#Sieve Of Erasthosthenes
def SieveOfErasthosthenes(n):
    prime = [False for i in range(n+1)]
    p = 2
    while(p*p<=n):
        for i in range(p*p,n+1):
            if i % p == 0:
                if not prime[i]:
                    prime[i] = True
        p+=1
    print(p)
    return prime
res = SieveOfErasthosthenes(50)
cnt = 0
for i in range(2,len(res)):
    if not res[i]:
        print(i, end=" ")
        cnt+=1
print()
print(cnt)