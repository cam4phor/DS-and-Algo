def findMin(self, nums):
    l = 0
    r = len(nums) - 1
    last = r
    ans = r
    while(l<=r): # why not <? wrong ans in case 2 
        mid = l + (r-l)//2
        if(nums[mid] < nums[last]):
            ans = mid
            r = mid - 1 
            # why go left -> becoz all the elems in left half 
            # are greater than last                     
            # elem and coming here proves                   
            # that we are in the right half, so we should 
            # go left to get the minimum of the right half
        else:
            l = mid + 1
            # why go right? -> becoz this means that we are 
            # in the left half and going right will 
            # only get us to the minimum of the group
    return nums[ans]
    