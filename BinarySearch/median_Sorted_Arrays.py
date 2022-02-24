# Naive approach -> 
# Merge the two arrays and find the median
# T -> O(n+m)
# S -> O(n+m)

# we can optimise the space as we already know where to divide and get the median elements in the sorted array
# this can be done by storing the values of the indexes where we are going to get the median

# Further optimisation can be done by changing the approach
# we already know that the arrays are sorted so we can try to apply Binary Search
# Now, how to apply binary search
# we already know how many elemets we need in the left half and right half inorder 
# to get the median

# lenght of the two arrays n1 and n2
# suppose the median is at position -> r = (n1 + n2)/2
# we know from the merge approach that, 
# in order to find the median all the elements in the left half should 
# be less than all the elements in the right half
# We are going to take x elements from the first array in the left half
# so we can only take r-x from the second array in the left half
# then we can go ahead and add a check for the correctness of the partition
# which would be if the last element from left partition of the first array (l1)
# is less than first element of the right partition of the second array (r2)
# and last element from the left partition of the second array (l2)
# is less than first element of the right partition of the first array (r1)
# then the partition holds good and we can find the median.


# if (l1 <= r2 and l2 <= r1)
# good partition
# if (l1 > r2):
# we need to decrease l1 so we need to go left (we are performing BS on 1st array)
# if (l1 < r2):
# we need to increase l1 so we need to go right
# if (l2 > r1):
# we need to increase r1 go right
# if (l2 < r1):
# go left


import math as math
import sys as sys
def findMedianSortedArrays(X, Y):
    m = len(X)
    n = len(Y)
    if(m > n) : return findMedianSortedArrays(Y, X)
    lower_bound = 0
    upper_bound = m
    median = 0
    while(upper_bound >= lower_bound):
        print("u = " + str(upper_bound))
        print("l = " + str(lower_bound))
        
        partitionX = (int)(math.floor((lower_bound+upper_bound)/2))
        partitionY = (int)(math.floor((m+n+1)/2)) - partitionX

        maxX = -sys.maxsize if(partitionX == 0) else X[partitionX-1]
        maxY = -sys.maxsize if(partitionY == 0) else Y[partitionY-1]

        minX = sys.maxsize if(partitionX == m) else X[partitionX]
        minY = sys.maxsize if(partitionY == n) else Y[partitionY]

        print("p_X = " + str(partitionX))
        print("p_Y = " + str(partitionY))
        print("max_X = " + str(maxX))
        print("max_y = " + str(maxY))
        print("min_X = " + str(minX))
        print("min_Y = " + str(maxY))
        if(maxX <= minY and maxY <= minX): #element found
            if(m+n)%2 == 0:
                median = (max(maxX, maxY) + min(minX, minY))/2
            else:
                median = max(maxX, maxY)
            break
        elif (maxX > minY): #go left
            print("going left")
            upper_bound = partitionX-1
        else: #go right
            print("going right")
            lower_bound = partitionX+1
    return median


A = []
B = [0, 23]

print(findMedianSortedArrays(A, B))
