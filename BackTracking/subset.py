A = [1, 2, 2]

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
# start from the first element and 
# choose to have it in the array(B) or not
# then splice the array from that element 
# and move to the next iteration of recursion
# starting from the first element again
# when the array becomes empty, append a copy of B
# to the answer and return.
def createSubsets(A, B, ans):
    #print(A)
    if(len(A) == 0):
        ans.append(B.copy())
        return
    # code to remove duplicates
    nextElem = 1
    createSubsets(A[nextElem:], B, ans)
    createSubsets(A[nextElem:], B+[A[0]], ans)

def subsets(nums):
    ans = []
    B = [[]]
    # duplicates
    for i in nums:
        for j in range(len(B)):
            B.append(B[j] + [i])
            

    #createSubsets(nums, B, ans)
    return B

print(subsets(A))