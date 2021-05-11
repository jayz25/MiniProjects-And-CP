#CODECHEF FEBRUARY LONG CHALLENGE
try:
    def conversionFunc(s):
        h, m = map(int,s[:-2].split(':'))
        j = s[-2:]
        h = h % 12 + (j.upper()=="PM")*12
        return (h+(m/60))
    for _ in range(int(input())):
        P = str(input())
        h, m = map(int,P[:-2].split(':'))
        p = P[-2:]
        h = h % 12 + (p.upper()=='PM')*12
        P = h+(m/60)
        #print(P)
        res = ''
        for i in range(int(input())):
            string = str(input())
            #print(string[:8],string[9:])
            #print(conversionFunc(string[:8]))
            #print(conversionFunc(string[9:]))
            if conversionFunc(string[:8])<=P and P<=conversionFunc(string[9:]):
                res+='1'
            else:
                res+='0'
        print(res)
except EOFError as e: 
    pass    
        
        