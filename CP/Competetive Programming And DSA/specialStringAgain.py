def specialString(n,s):
    i = 0
    result = 0
    while(i<n):
        char_count = 1
        while(i+1<n and s[i]==s[i+1]):
            i+=1
            char_count+=1
    result+=int(char_count*(char_count+1)/2)
    for i in range(1,n):
        char_count = 1
        while(i-char_count>-1 and i+char_count<n and s[i-char_count]==s[i+char_count] and s[i-char_count]!=s[i] and s[i-1]==s[i-char_count]):
            char_count+=1

    result+= char_count-1
    return result

            