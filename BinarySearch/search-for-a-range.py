#search-for-a-range
def searchRange(A, B):
    pos = [-1, -1]
    n = len(A)
    if (n==0):
        return pos
    low = 0
    high = n-1
    mid = 0
    ans = -1
    # Sept 2021
    # initial Position
    # if we find the element store the pos and move to the left.
    # here we cannot combine A[mid] == B and A[mid] > B, as we have to store -1 in one cases

    # Jan 2022
    # we need to find the first True both in the left and the right side
    # for initial pos -> 
    # if we find an element greater than or equal to B
    #    we store the answer and go to the left to find a tighter bound
    # else we go to the right
    # why not less than or equal to?
    #    because in if A[mid] <  B -> we need to go right
    #           and if A[mid] == B -> we need to go left for the initial pos
    while (high >= low):
        mid = low + (high-low)//2
        if(A[mid] >= B):
            ans = mid
            high = mid - 1
        else: low = mid + 1
    pos[0] = ans if (A[ans] == B) else -1
    low = 0
    high = n-1
    mid = 0
    ans = -1
    # Sept 2021
    # final position
    # if we find the element store the pos and move to the right
    # here we cannot combine A[mid] == B and A[mid] < B, as we have to store -1 in one cases
    # We have an explicit case so we cannot combine the two cases.

    # Jan 2022
    # we need to find the first True both in the left and the right side
    # for final pos -> 
    # if we find an element less than or equal to B
    #    we store the answer and go to the right to find a tighter 
    # else we go to the left
    # why not greater than or equal to ?
    #    because in if A[mid] >  B -> we need to go left
    #           and if A[mid] == B -> we need to go right for the final pos
    while(high >= low):
        mid = low + (high-low)//2
        if(A[mid] <= B):
            ans = mid
            low = mid+1
        else: high = mid-1
    pos[1] = ans if (A[ans] == B) else -1

    print(pos)

A = [1, 4, 8, 8, 8, 8, 9, 10, 12, 15]
    #F  F  T  T  T  T  F  F   F   F
B = 7

searchRange(A, B)