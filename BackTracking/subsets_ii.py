A = [3, 1, 2, 2, 2, 2, 3, 3, 3]

# Same as subsets but the only difference is that
# when there is a duplicate we are only adding the duplicate number
# at the end of the array added in the previous iteration of the loop.
# this allows us to have non duplicate values
# we need to sort the initial array, btw.

def subsets(nums):
    nums.sort()
    B = [[]]
    # duplicates
    startpos = 0
    nextStartPos = 0
    for index, i in enumerate(nums):
        if(i > 0 and nums[index] == nums[index-1]):
            startpos = nextStartPos
        else:
            startpos = 0
        nextStartPos = len(B)
        for j in range(startpos, len(B)):
            B.append(B[j] + [i])
    #createSubsets(nums, B, ans)
    print(len(B))
    return B

print(subsets(A))
