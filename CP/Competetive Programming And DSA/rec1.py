def numbers(n):
    if n==0:
        return
    numbers(n-1)
    print(n)
N = int(input())
numbers(N)