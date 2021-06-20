#N = int(input())
N = 5
arr = ["HARI","HARRY","LATA","SARAH","LALA"]
#arr = list(map(int,input().split()))
set_array = []
for string in arr:
    set_array.append(set(string))
set_array.sort(key=lambda x:x[1])
print(set_array)