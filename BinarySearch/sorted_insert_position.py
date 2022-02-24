def solve(A, B):

    n = len(A)
    if(n == 0):
        return -1
    low = 0
    high = n-1
    mid = 0
    ans = -1
    while (high >= low):
        mid = low + (high - low)//2
        if(A[mid] >= B):
            # we can store the number here
            # but we have to go left to find the right fit.
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

# need to find the smallest element larger than or equal to x
# This can be used to implement insertion sort


A = [1, 3, 5, 6]
    #T  T  F  F
# if we find the element, we need to find the first true
# else we need to find the first false

B = 5
print (solve(A, B))
