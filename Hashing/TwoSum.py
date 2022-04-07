A = [2, 4, 2, 3, 2]
B = 4

# element x at i and element B - x at j should be present in the array
# so we hash every element such that in the hash, we have values in the form
# {target - x, index} so, if we encouter y such that y = target-x, then 
# it will be in the array and we have both the indices at that point of time. 

def TwoSum(A, B):
  dict_H = {}
  for i in range(len(A)):
    if(A[i] in dict_H): # always use key in dict for better results
      return [dict_H[A[i]], i]
    dict_H[B-A[i]] = i
    

print(TwoSum(A, B))