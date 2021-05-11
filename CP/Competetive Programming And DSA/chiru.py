t = int(input())
while(t!=0):
    
    n=int(input())
    print(3, end='')
    for i in range(1,n):
        if i % 2 == 0:
            print(' %d' %(i*2),end='')
        else:
            print(' %d' %(i**2),end='')
    t=-1
    print()
    
