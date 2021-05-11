from itertools import permutations
'''
def stringPermutation(string):
    permutation = [''.join(p) for p in permutations(string)]
    return permutation
'''
def stringPermutation(lst):
    if len(lst)==0:
        return []
    if len(lst)==1:
        return [lst]
    l = []

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i+1:]

        for p in stringPermutation(remLst):
            l.append([m]+p)

    return l





string = str(input())
data = list(string)
print(stringPermutation(data))
result = stringPermutation(data)
for i in result:
    print(''.join(i),end=" ")