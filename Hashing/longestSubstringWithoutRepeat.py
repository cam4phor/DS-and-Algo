# 7 April, 2022

# We store the previous occurance of all the characters
# if we come accross a character then we update the start
# to the next of the previous same character (hence storing i+1)
# update start only if start is less than previous index of similar character
# else we will end up leaving a scenario where elems between two endpoints are repeating.




def lswr(s):
  dict_h = {}
  start = 0
  count = 0
  maxC = 0
  for i in range(len(s)):
    if(s[i] in dict_h):
      start = max(start, dict_h[s[i]])

    dict_h[s[i]] = i+1
    count += 1
    maxC = max(count-start, maxC)
  return maxC

s = "chiragroshanvaswani"
print(lswr(s))
