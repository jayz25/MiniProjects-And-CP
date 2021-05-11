def decimalToBinary(n):  
    return print(format('{:08b}'.format(n)))
t = int(input())
while(t!=0):
    n=int(input())
    decimalToBinary(n)
    t-=1