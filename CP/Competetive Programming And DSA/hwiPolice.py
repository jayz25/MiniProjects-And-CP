n = int(input())
k = int(input())
arr = [0,1,0,0,1,0]
stack = []
i = 0
while(i<n):
    if arr[i]==0:
        stack.append(i+1)
        print(stack)
        i += 1
    else:
        for _ in range(k):
            try:
                stack.pop()
            except IndexError:
                pass
            print("for",stack)
        stack.append(i+1)
        i = i + 1
print(sum(stack))    
