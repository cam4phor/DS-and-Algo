
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