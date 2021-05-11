sum = 0
def dec_bin(n):
    if n==0:
        sum = 0
        return sum
    else:
        dec_bin(n//2)
        sum = sum*10 + (n%2)
    return sum
t = int(input())
while(t!=0):
    n = int(input())
    dec_bin(n)
    print(sum)
    sum=0
    print()