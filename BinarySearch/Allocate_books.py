# We need to allocate the books in contiguous order such that
# the maximum pages allocated to anyone is minimum

# Approach
# We are given contiguous ordering hence we can do a summation
# Maximum pages to any single person can be the sum(arr), because then all the books go 
# to one person
# Minimum value that we can get for an answer is max(arr), when we have the number of books 
# equal to the number of students

# here the range is 90 to 204

# Now we can iterate from 90 to 204 and check if we can really allocate
# for 90 (as the max value that can be allocated to a single person)
# we can give 12 (not greater than 90)
# we can give 34 (12+34 = 46) (not greater than 90)
# we cannot give 67 (as 113 > 90) so we move forward to the second student

# for student 2
# we can only give 67

# for student 3
# we can only give 90

# but here we required 3 students to allocate all the books
# hence this answer is not possible

# Now we can do the same thing for 204
# but we will get 1 as the answer and no one else will get any books
# so not possible

# We can go to the middle 147
# student 1 will get 12+34+67 = 113
# student 2 will get 90

# we were able to divide the books hence this is a possible answer
# Since this is a possible answer, we can rule out all the possible answers which are greater than 147
# as we will always get this answer for values greater than 147 and we want minimum

# now the range is 90 - 147
# middle -> 117
# same result as the previous iteration

# now range is 90 - 117
# mid -> 103
# now we would need 3 students and hence we cannot go here
# so we increase the low value

# range -> 103 - 117
# mid -> 110
# 3 students again

# 110 - 117
# mid - 113
# 2 students

# 110 - 113
# mid 111
# 3 students

# 111 - 113
# mid 112
# 3 students

# 112 - 113
# mid 112
# 3 students

def canAllocateBooks(A, mid):
    sum = 0
    n = 0 # splits
    for i in A:
        if(sum + i > mid):
            sum = 0
            n += 1
        sum += i
    return n


A = [1,2,3,4,5,6,7,8,9,10]
B = 5

low = max(A)
high = sum(A)

while (high >= low):
    mid = low + (high - low)//2
    if (canAllocateBooks(A, mid) >= B): 
        # why greater than or equal to ->
        # because when we get the required number of students
        # we need to tighten the lower bound such that 
        # we find the point beyond which we cannot go lower
        low = mid + 1
    else:
        high = mid - 1

# low will be our answer in this case
print (low)
print (high)
print (mid)