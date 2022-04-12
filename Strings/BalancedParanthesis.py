S = '[]]]'

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
    
      

