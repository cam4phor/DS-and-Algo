
n = "34"


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
  loops = 1
  tempArr = []
  for i in range(len(str)-1, -1, -1):
    tempArr.append(dict_nums[str[i]])
  arr = []
  arr2 = []
  for i in range(len(tempArr)):
    for j in range(len(tempArr[i])):
      if(i == 0):
        arr.append(tempArr[i][j])
      else:
        for k in range(len(arr)):
          arr2.append(tempArr[i][j]+arr2[k])
    arr2 = arr
  print(len(arr2), arr2)
    
getCombinations(n)