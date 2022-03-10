def combinations(arr, ans, comb_arr, k, index):
    if(index == len(arr)):
        if(k == 0):
            ans.append(comb_arr)
        return
    # Choose the current element and reduce k.
    combinations(arr, ans, comb_arr+[arr[index]], k-1, index+1)
    # Don't choose the current element.
    combinations(arr, ans, comb_arr, k, index+1)
    
        

n = 4
k = 3
arr = [i+1 for i in range(n)]
print(arr)
ans = []
combinations(arr, ans, [], k, 0)
print(ans)