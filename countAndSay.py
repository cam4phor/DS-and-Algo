s = 111221

# brute force approach
# at every iteration we have the previous number
# we append a dummy char at the end of this string
# because we need to look for i+1'th element when we
# looping accross
# When we are inside the loop we check if the next character
# is equal to the this character
# if it is not we append it to the number along with the string value and
# we make the count to zero 
# and we increase the count in every iteration 

def countAndSay(n):
  s = '1e'
  ans = 0
  while(n-1):
    count = 0
    number = ''
    for i in range(len(s)-1):
      count+=1
      if(s[i+1] != s[i]):
        number += str(count) + s[i]
        count = 0
    ans = int(number)
    number += 'e'
    s = number[:]
    number = ''
    n-=1
  
  return ans

print(countAndSay(7))
