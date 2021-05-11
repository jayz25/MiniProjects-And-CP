def isPalindrome(string):
    ls = list(string)
    ls1 = [ls[x] for x in range(len(ls)-1,-1,-1)]
    if ls==ls1:
        return 'Yes'
    else:
        return 'No'
'''
Another Way 
return s ==s[::-1]
'''
'''
Aother way 
rev= ''.join(reversed(s))
    if s==rev:
        return True
    return False
'''
'''
Another Way
    for i in range(0,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
'''


string = str(input())
print(isPalindrome(string))