def removeChar(string,r):
    ls = list(string)
    ls.remove(r)
    rev = ''.join(ls)
    print(len(rev))
    return rev
    
string = str(input())
r = str(input())
print(removeChar(string,r))
