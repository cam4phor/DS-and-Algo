# Feb 26, 2022
# iterate through the array provided
# for each item, remove it from current array and 
# add it to another array
# untill the array is empty
# then store the final answer
# then back track
# by restoring the removed element from the same position
# from which it was cleared

A = [1, 2, 3, 5]

B = []
ans = []
def permutations(A, B):
    if len(A) == 1:
        B.append(A[0])
        ans.append(B.copy())
        B.pop()
        return

    for i in range(len(A)):
        elem = A[i]
        B.append(elem)
        del A[i]
        permutations(A, B)
        A.insert(i, elem)
        del B[len(B)-1]


permutations(A, B)
print(ans)

