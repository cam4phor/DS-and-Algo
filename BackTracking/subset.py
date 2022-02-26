A = [1, 2, 3, 4]

# def printSubsets(A, K, P, i, x):
#     if (i >= len(A)-1):
#         if(x == True): K.append(A[i])
#         P.append(K.copy())
#         if (x == True): K.pop()
#         return
#     if(x == True):
#         K.append(A[i])
#         printSubsets(A, K, P, i+1, False)
#         printSubsets(A, K, P, i+1, True)
#         K.pop()
#     elif(x == False):
#         printSubsets(A, K, P, i+1, False)
#         printSubsets(A, K, P, i+1, True)

    

# def subSets(A):
#     K = []
#     P = []
#     printSubsets(A, K, P, 0, False)
#     printSubsets(A, K, P, 0, True)
#     P.sort()
#     return P

# print(subSets(A))

# Feb 26, 2022
def createSubsets(A, B, ans):
    #print(A)
    if(len(A) == 0):
        ans.append(B.copy())
        return
    
    createSubsets(A[1:], B, ans)
    createSubsets(A[1:], B+[A[0]], ans)
            
def subsets(nums):
    ans = []
    B = []
    createSubsets(nums, B, ans)
    return ans

print(subsets(A))