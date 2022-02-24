import math as math
def search(A, B):
    n = len(A)
    if (n == 0):
       return -1
        
    low = 0
    high = n-1
    mid = 0
    first = A[0]
    while (low <= high):
        print ("new")
        print (high)
        print (low)
        mid = low + (high - low)//2
        print (mid)
        if(A[mid] == B):
            return mid
        num_is_big = (B >= first)
        mid_is_big = (A[mid] >= first)
        if(num_is_big == mid_is_big):
            # number in the same half as we are
            if(A[mid] > B):
                high = mid - 1
            else:
                low = mid + 1
        else:
            # number not in the same half as we are
            # here we just need to calibrate the search such that we 
            # end up in the correct half in the next iteration
            if(num_is_big):
                high = mid - 1
            else:
                low = mid + 1
                
    return -1
A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 0
print(search(A, B))



# Here first we categorize whether our pointer and target are in the same
# half or not
# First of all there are two halves
# Both of them are having elements in non-decresing order (as there can be duplicates)
# Just that, one half is having all the elements which are less than the other half
# So to figure (and the target) out whether our pointer is in the first half or the second
# we compare it with the first element of the array and store the boolean result in 
# a variable num_is_big and mid_is_big
# If both of them are equal that means both the pointer and target are in the same half
# In that case we can apply normal Binary Search
# In the other case ( when the variable mismatch )
# we can tame the pointer to come to the half where the element lies
# by checking in which half it is present currently
# then moving it to correct half based on the condition and position