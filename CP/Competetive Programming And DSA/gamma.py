def solve(A,B):
    if A==B:
        return True
    if len(A)<=1:
        return False
    n = len(A)
    flag = False
    for i in range(1,n):
        if ((solve(A[:i],B[-i:])==True and solve(A[i:n-i],B[n-i:i])==True) or (solve(A[:i],B[:i])==True and solve(A[i:n-i],B[i:n-i])==True))==True:
            flag = True
            break
        return flag



if len(A)!=len(B):
    print(False)
print(len(A),len(B))
print(solve(A,B))