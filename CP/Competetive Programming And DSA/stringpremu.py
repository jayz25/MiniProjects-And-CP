from itertools import permutations
def stringPermutation(string):
    permutation = [''.join(p) for p in permutations(string)]
    return permutation

string = str(input())
print(stringPermutation(string))