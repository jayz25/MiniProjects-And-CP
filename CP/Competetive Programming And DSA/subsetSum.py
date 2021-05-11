# Python3 implmentation to find the 
# minimum number of sequence 
# required from array such that 
# their sum is equal to given S 

# Function to find the count of 
# minimum length of the sequence 
def Count(S, m, n): 
	table = [[0 for i in range(n + 1)] 
				for i in range(m + 1)] 

	# Loop to intialize the array 
	# as infinite in the row 0 
	for i in range(1, n + 1): 
		table[0][i] = 10**9 - 1

	# Loop to find the solution 
	# by pre-computation for the 
	# sequence 
	for i in range(1, m + 1): 

		for j in range(1, n + 1): 
			if (S[i - 1] > j): 
				table[i][j] = table[i - 1][j] 
			else: 

				# Minimum possible 
				# for the previous 
				# minimum value 
				# of the sequence 
				table[i][j] = min(table[i - 1][j], 
								table[i][j - S[i - 1]] + 1) 

	print(table) 

# Driver Code 
if __name__ == '__main__': 
	arr= [9, 6, 5, 1] 
	m = len(arr) 
	Count(arr, m, 11) 

# This code is contributed by Mohit Kumar 
