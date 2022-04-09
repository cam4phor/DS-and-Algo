
s = "acdb"
def findLps1(s, count):
  count[0] = s[0]
  Arr = [[0 for i in range(len(s))] for j in range(len(s))]

  for i in range(len(s)):
    Arr[i][i] = 1
    if(i<len(s)-1):
      if(s[i] == s[i+1]):
        Arr[i][i+1] = 1
        if(len(count[0])<2):
          count[0] = s[i:i+2]
      else:
        Arr[i][i+1] = 0
  
  i = 0
  k = 2
  j = i + k 
  while(i != 1 and j != len(s)):
    while(j != len(s)):
      if(s[i] == s[j]):
        Arr[i][j] = Arr[i+1][j-1]
        if(j-i+1 > len(count[0]) and Arr[i][j]):
          count[0] = s[i:j+1]
      else:
        Arr[i][j] = 0
      i+=1
      j+=1
    k += 1
    i = 0
    j = i + k



  # for i in range(len(s)):
  #   for j in range(i+2, len(s)):
  #     if(s[i] == s[j]):
  #       Arr[i][j] = Arr[i+1][j-1]
  #       if(j-i+1 > len(count[0]) and Arr[i][j]):
  #         count[0] = s[i:j+1]
  #     else:
  #       Arr[i][j] = 0    

  for i in range(len(s)):
    print(Arr[i])  
      

def findLps(s, first, last, d, count):
  str_i = s[first: last+1]

  if(str_i in d):
    return d[str_i]

  if(first > last):
    return True

  if(first == last):
    d[str_i] = True
    if(last - first + 1 > len(count[0]) and d[str_i]):
      count[0] = str_i


  if(s[first] == s[last]):
    d[str_i] = findLps(s, first+1, last-1, d, count, True)
    if(d[str_i] and last - first + 1 > len(count[0])):
      count[0] = str_i
    return d[str_i]
  d[s[first: last]] = findLps(s, first, last-1, d, count)
  d[s[first+1: last+1]] = findLps(s, first+1, last, d, count)


def lps(s):
  first = 0
  last = len(s)-1
  count = [""]
  d = {} # {str: Boolean}
  # findLps(s, first, last, d, count)
  findLps1(s, count)
  for i in d.keys():
    print(i, d[i])

  print(len(count[0]), count)

lps(s)
  
