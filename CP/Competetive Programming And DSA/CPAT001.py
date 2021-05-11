from itertools import permutations
try:
    for _ in range(int(input())):
        string = str(input())
        og = 'PCM'
        ls = [''.join(x) for x in list(permutations(og))]
        if string in list(ls):
            print('YES')
        else:
            print('NO')
except EOFError as e:
    pass