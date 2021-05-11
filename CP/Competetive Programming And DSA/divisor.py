#CODECHEF FEBRUARY LONG CHALLENGE DIVISOR
try:
    n = int(input())
    for i in range(10,0,-1):
        if n % i==0:
            print(i)
            break
except EOFError as e:
    pass