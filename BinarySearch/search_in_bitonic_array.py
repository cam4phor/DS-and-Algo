
def search(A, B, l, r):
    bPoint = -1
    l = 0
    r = len(A)-1
    while(l<=r):
        mid = l + (r-l)//2
        if(A[mid-1] < A[mid]):
            bPoint = mid
            l = mid+1
        else:
            r = mid-1
    print(bPoint)

    # while(l<r):
    #     mid = l + (r-l)//2
    #     if (mid > 0 and mid < len(A)-1):
    #         if(A[mid-1] > A[mid] and A[mid+1] < A[mid]):
    #             # right side
    #             r = mid -1 
    #         elif (A[mid-1] < A[mid] and A[mid+1] > A[mid]):
    #             # left side
    #             l = mid + 1
    #         else:
    #             bPoint = mid
    #             # Bitonic Point

    l = 0
    r = bPoint if bPoint != -1 else len(A)-1
    while(l < r):
        mid = l + (r-l)//2
        if (A[mid] == B):
            return mid
        elif (A[mid] > B):
            r = mid - 1
        else:
            l = mid + 1

    l = bPoint if bPoint != -1 else 0
    r = len(A)-1
    while(l<r):
        mid = l + (r-l)//2
        if (A[mid] == B):
            return mid
        elif (A[mid]<B):
            r = mid - 1
        else:
            l = mid + 1


    return -1

def solve(A, B):
    #using 1 level Back Tracking -> can't really be done as we do not know the position of the largest element
        # we can first locate the largest element then we can find in both the arrays ---- NOT GOOD SOLN
    
    # can check if we are in the left side or the right side by checking the left and right elems -- Hacky way
    # after the first iteration, are we sure that we are either on the left side or the right side
    # but this is becoming more and more the approach where we divide the arrays

    elem = search(A, B, 0, len(A)-1)
    print(elem)





A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    #0  1  2  3  4  5   6  7  8
#       +  +  +  +  +   -  -  -
B = 12
solve(A, B)