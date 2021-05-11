from collections import Counter
def nonrepeat(string):
    d = {}
    char_order = []
    for i in string:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
            char_order.append(i)
    for c in char_order:
        if d[c] == 1:
            return c

    
    
    


string = str(input())
print(nonrepeat(string))