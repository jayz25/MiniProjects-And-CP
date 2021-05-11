def maxSum(arr):
    l = len(arr)
    max_so_far = -99999999
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(l):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
arr = [-2, -3, 4, -1, -2, 1, 5, -3]