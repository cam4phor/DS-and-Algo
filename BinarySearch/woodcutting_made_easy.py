def cutPartLength(A, height):
    sum = 0
    for i in A:
        sum += ((i - height) if i >= height else 0)
        
    return sum
# Requirements for Binary Search
# We need a Range(Sorted) and a Target. That's it!!!
# Here the Range is 0 to max(A).
# and Target is B which has to be found out by adding a condition usually but here we need to write a Func.


def solve(A, B):
    if(len(A) == 0):
        return 0

    low = 0
    high = max(A)
    mid = 0
    ans = 0
    while (low <= high): #comeback
        print("new")
        print ("low " + str(low))
        print ("high " +str(high))
        mid = low + (high - low)//2
        x = cutPartLength(A, mid)
        print("x = " +str(x))
        print("mid = "+ str(mid))
        if(x>=B):
            ans = mid
            low = mid + 1
        else: high = mid-1
    
    return ans


A = [ 20, 15, 10, 18]
B = 7

# here a person can cut either 0 or the max height of the tree in the given array
# we need to find a number between 0 and max(A) such that we optimize the result so 
# that we only cut what is required.
# so for each iteration we calculate what we get by subtracting from each input of the array
# then we check if what we got is >= what we want -> if yes, we store the answer and go right 
# to find a tighter fit.
# else we go right
print(solve(A, B))
