S = '[]]]'
# easy problem;
# check for opening braces first and add that into an array
# match braces and if the closing bracket appears remove a bracket from arr
# if a closing bracket appears first return 0
# If at the end of all the array still has something return 0
# if the array has nothing return 1

def checkIfBalanced(s):
  arr = []
  for i in range(len(s)):
    if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
      arr.append(s[i])
    x = ""
    if(arr):
      if(s[i] == ")"):
        x = arr.pop()
        if(x != "("):
          return 0
      elif(s[i] == "]"):
        x = arr.pop()
        if(x != "["):
          return 0
      elif(s[i] == "}"):
        x = arr.pop()
        if(x != "{"):
          return 0
    else:
      return 0

  if(arr):
    return 0
  return 1

print(checkIfBalanced(S))
    
      

