# Given an integer array A of size N containing 0's and 1's only. 

# You need to find the length of the longest subarray having count of 1’s one more than count of 0’s.

A = [0, 1, 1, 0, 0, 1]


# dictionary -> {sum: i}
# insert into dictionary only when sum is not in the dictionary
# basic concept is that if sum is there in the dict
# and we have sum-1 as well, so from index of sum-1 to index of sum
# we have added one 1.
# Hence we can get the count by subtracting index of sum and sum-1
# If sum >= 1, we can directly store the index of current element.

def FindLCL(A):
  dict_L = {}
  sum = 0
  max = -1
  for i in range(len(A)):
    sum += 1 if A[i] == 1 else -1
    if(sum not in dict_L.keys()):
      dict_L[sum] = i
    
    if(sum-1 in dict_L):
      if(i - dict_L[sum-1] > max):
        max = i - dict_L[sum-1]
    
    if(sum >= 1):
      if(i + 1 > max):
        max = i + 1
  print(dict_L)
  return max

print(FindLCL(A))
    