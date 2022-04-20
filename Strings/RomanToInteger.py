# April 16,
# Store the value of roman numerals and numbers in a dictionary
# if the next number is greater than the current number
# subtract from value
# if the next number is less than the current number
# Add to the value;


roman = {
  "I": 1,
  "V": 5,
  "X": 10, 
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}

str_i = "VX"

def romanToInt(s):
  val = 0
  for i in range(len(s)-1):
    if(roman[s[i+1]] > roman[s[i]]):
      val -= roman[s[i]]
    else:
      val += roman[s[i]]
  val += roman[s[len(s)-1]]

  return val

print(romanToInt(str_i))