# feb 27, 2022;

# Mostly the code is same but 
# what we are doing here is a neat trick to avoid similar recursion trees
# in case where we have duplicate elements in the starting array
# In that case, if we are ignoring one element which has a duplicate in the list
# we might as well ignore all the succeeding duplicates and move on
# NEAT!!!
arr = [1]*25
target = 25
def findCombination(arr, comb_arr, target, ans, i):
    # if(i>0 and arr[i] == arr[i-1]):
    #     return
    # cur_sum = sum(comb_arr)
    if (i > len(arr)-1):
        if target == 0:
            ans.append(comb_arr.copy())
        return
    addToNext = 1
    j = i
    while(j+1<len(arr)):
        if(arr[j+1] == arr[j]):
            addToNext+=1
        else:
            break
        j+=1
    findCombination(arr, comb_arr, target, ans, i+addToNext)
    if(arr[i] <= target):
        findCombination(arr, comb_arr + [arr[i]], target-arr[i], ans, i+1)


ans = []
comb_arr = []
print(len(arr))
arr.sort()
findCombination(arr, comb_arr, target, ans, 0)
# ans.sort()
# i = 1
# while(i < len(ans)):
#     if(ans[i] == ans[i-1]):
#         ans.pop(i)
#     else:
#         i+=1
for i in ans:
    print(i)
