t = int(input())
while(t!=0):
    x, y = map(int,input().split())
    samplespace = x + y
    probability = x/samplespace
    print(probability)