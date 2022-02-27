# arr = [ 8, 10, 6, 11, 1, 16, 8 ]
# target = 28

# def findSubset(A, cur_ind, B, K, P):
#     if (cur_ind == len(A)):
#         if (B == 0):
#             K.sort()
#             P.append(K.copy())
#         return
#     if(A[cur_ind] <= B):        
#         K.append(A[cur_ind])
#         findSubset(A, cur_ind, B-A[cur_ind], K, P)
#         K.pop()
#     findSubset(A, cur_ind+1, B, K, P)


# cur_ind = 0
# K = []
# P = []
# cur_sum = 0
# A.sort(reverse = True)
# A.sort()
# i = 1
# while i < len(A):
#     if A[i] == A[i-1]:
#         A.pop(i)
#     else:
#         i += 1
# findSubset(A, cur_ind, B, K, P)
# P.sort()
# print(len(P))
# for i in P:
#     print(sum(i))
#     print (i)





#Feb 27, 2022
# for each recursion iteration 
# consider the current element or don't consider it
# there is no condition to 'not consider'
# but to consider an element, current_sum + current element should be less than target
# when we consider the current element, there is a possibity that 
# we would need it again so we don't increase the iterator.
# and the recursion starts afresh.
arr = [ 8, 10, 6, 11, 1, 16, 8 ]
target = 28

def findCombination(arr, comb_arr, target, ans, i):
    cur_sum = sum(comb_arr)
    if (i > len(arr)-1):
        if (cur_sum == target):
            ans.append(comb_arr.copy())
        return
    
    findCombination(arr, comb_arr, target, ans, i+1)
    if(cur_sum + arr[i] <= target):
        findCombination(arr, comb_arr + [arr[i]], target, ans, i)
    # else:
    #     findCombination(arr, comb_arr, target, ans, i+1)
        


    
ans = []
comb_arr = []
findCombination(arr, comb_arr, target, ans, 0)
for i in ans:
    print(i)

