def lcs(X,Y,m,n):
    L = [[0 for x in range(n+1)]for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    print(L)
    index = L[m][n]

    lcstr = [""]*(index+1)
    lcstr[index] = ""
    
    i = m
    j = n
    while i>0 and j>0:
        if X[i-1] == Y[j-1]: # if equal then simply go to previous diagonal
            lcstr[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]: # if not equal then go to  previous greater between adjacent in table 
            i-=1
        else:
            j-=1
        
        
    print(L[m][n],lcstr)

X= "AGGTAB"
Y= "GXTXAYB"
m = len(X)
n = len(Y)
lcs(X,Y,m,n)