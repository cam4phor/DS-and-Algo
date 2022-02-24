def solve(A, B):
    n = len(A)
    if(A[n-1] <= B): return n
    if(n == 0): return 0
    low = 0
    high = n - 1
    ans = -1
    while(high >= low):
        mid = low + (high-low)//2
        if (A[mid] <= B):
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    return ans


A = [0, 0, 0, 1, 2, 3, 3, 3, 4, 7, 8, 8, 9]
    #0  1  2  3  4  5  6  7  8  9 10 11 12
#3  #T  T  T  T  T  T  T  T  F  F  F  F  F

    # need to find the first false

    # for 3, if we find it in the array we move 
    # to the right and once we find something greater 
    # that that number we store it and move to the left.
    # Find smallest number larger than x
B = 8
print(solve(A, B))


    
