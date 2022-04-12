A = [-1, 0, 1, 0, -2, 2, -2, 4, -2, 4]

def findThreeSum(A):
  A.sort()
  print(A)
  arr = []
  for i in range(len(A)): 
    if (i > 0 and A[i] == A[i-1]):
      continue                    # O(n)
    sumReq = 0 - A[i]             # O(1)

    l = i+1 
    r = len(A)-1
    while(l<r):
      if(A[l] + A[r] == sumReq):
        arr.append([A[i], A[l], A[r]])
        l+=1
        while(l < r and A[l] == A[l-1]):
          l+=1
      elif (A[l] + A[r] < sumReq):
        l+=1
      else:
        r-=1
    
                    # O(1)
    # for j in range(i+1, len(A)): 
    #   if(A[j] in dict_A):         # O(1) best case, O(n) worst case
    #     # make team
    #     x = [A[i], A[dict_A[A[j]]], A[j]]
    #     arr.append(x.copy())
    #     while(j < len(A) and A[j] == A[j-1]):    # Avoid duplicates
    #       j+=1
        
    #   elem = sumReq - A[j]
    #   if(elem not in dict_A):
    #     dict_A[elem] = j
  # arr.sort()
  print(arr)



findThreeSum(A)