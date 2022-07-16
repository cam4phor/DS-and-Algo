def maxKSubarraySum(A, k) -> int:
	array = A
	if (k == len(array)): return sum(array)
	if (k == 1): return max(array)

	sum_1 = 0
	for i in range(k):
		sum_1 += array[i]
		
	cur_sum = sum_1
	for i in range(1, len(array)):
		
		if(i+k <= len(array)):
			cur_sum += array[i+k-1]
			cur_sum -= array[i-1]
			if(cur_sum > sum_1):
				sum_1 = cur_sum

	return sum_1


# logic ->
# add the current element and remove the last element while going through the array
