def longestPalindrome(string):
    if(string==None or len(string)==0):
        return ''
    startt = 0 
    endd = 0
    for i in range(len(string)):
        len1 = expandFromMid(string,i,i)
        len2 = expandFromMid(string,i,i+1)
        l = max(len1,len2)
        if(l> endd-startt):
            startt = i - ((l-1)/2)
            endd = i + (l/2)
    return string[startt:endd+1]
def expandFromMid(string,left,right):
    if(string==None or left>right):
        return 0
    while(left>=0 and right < len(string) and string[left]==string[right]):
        left-=1
        right+=1
    return right-left-1
    
string = 'forgeekskeegfor'
print(longestPalindrome(string))








string = str(input())
print(logestPalindrome(string))