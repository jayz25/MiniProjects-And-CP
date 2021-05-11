#Kadane's Algorithm.. Maximum subarray 
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    current_sum = 0
    best_sum = 0
    for i in arr:
        current_sum = max(0,current_sum+i)
        best_sum = max(best_sum,current_sum)
    print(best_sum)