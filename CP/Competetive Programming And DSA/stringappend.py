def stringAppend(string,c,n):
    l = len(string)
    newstring = c*n
    print(newstring)
    res = string[:l//2] + newstring + string[l//2:]
    print(res)



string = str(input())
c = str(input())
n = int(input())
stringAppend(string,c,n)