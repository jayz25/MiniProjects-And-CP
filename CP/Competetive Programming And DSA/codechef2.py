"""
T
N
S
"""
T = int(input())
while T!=0:
    code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    N = int(input())
    S = str(input())
    ans = ''
    for i in range(N):
        
        if i%4==0 and i!=0:
            ans+= code[0]
            code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        l = len(code)//2
        if S[i]=='0':
            code=code[:l]
        else:
            code=code[l:]
    ans+= code[0]
    print(ans)
    T-=1