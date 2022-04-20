# read the string from left to right
# add the corresponding letters possible
# with the current letter in an array (tempArr). (add 'abc' for 2)
# initialize an empty array arr
# for each value in the tempArr
# initialize an empty array (again) (arr2)
# Go through each item "item" in the tempArr (if we have abc we go through a, b and c separately)
# for each letter go through the entire array "arr"
# and prepend "item[i]" to each item in the array and add the final string to "arr2"
# when all items in tempArr and arr are done assign arr2 to arr


# we need the final array sorted, so we can use a trick for that
# when we have "23" as an input, we have ["abc", "def"] as the temp array
# so the final if we go through the above algorith would be ["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"]
# so if we reverse the temp array we'll get the correct sorted order

n = "2347"


def getCombinations(str):
  dict_nums = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
  }
  tempArr = []
  for i in range(len(str)-1, -1, -1):
    tempArr.append(dict_nums[str[i]])
  arr = ['']
  for i in range(len(tempArr)):
    arr2 = []
    for j in range(len(tempArr[i])):
      for k in range(len(arr)):
        arr2.append(tempArr[i][j] + arr[k])
        # print(arr)
    arr = arr2
    # for j in range(len(tempArr[i])):
    #   if(i == 0):
    #     arr.append(tempArr[i][j])
    #   else:
    #     for k in range(len(arr)):
    #       arr2.append(tempArr[i][j]+arr[k])
  print(len(arr), arr)
    
getCombinations(n)