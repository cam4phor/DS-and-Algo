A = [1, 2, -3, 3]
# Mar, 14
# We know that Sum(i, j) = Sum(j) - Sum(i-1)
# Now we need to find the range(i, j) where the sum is 0
# hence find i and j such that Sum(j) = Sum(i-1)

# Why are we concerned about the sum
# because while traversing the array, we can store
# the info of the previous element in the sum
# And store the the index of the current element in a
# dictionary such that dict[sum] = index
# then if the dictionary already contains a particular sum
# compare the distance of the range.


def lsZero1(A):
    Sum = {}
    max = 0
    final = 0
    initial = 0
    Sum[0] = -1
    cur_sum = 0
    for i in range(len(A)):
        cur_sum += A[i]
        if(cur_sum in Sum.keys()):
            if(i - Sum[cur_sum]+1 > max):
                max = i - Sum[cur_sum]+1
                final = i
                initial = Sum[cur_sum]
        else: 
            Sum[cur_sum] = i
    
    if(final == initial and A[final] != 0): return []
    return A[initial+1: final+1]
    



# Brute force DP
def lsZero(A):
    B = [[-1]*len(A)]*len(A)
    # print(B)
    max = -1
    initial = 0
    final = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if(j==i):
                B[i][i] = A[i]
            else:
                B[i][j] = B[i][j-1] + A[j]
            if(B[i][j] == 0 and j-i+1>max):
                max = j-i+1
                initial = i
                final = j
    print(final)
    print(initial)
    if(final == initial and A[final] != 0): return []
    return A[initial: final+1]

print(lsZero1(A))
            