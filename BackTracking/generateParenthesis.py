# We use backtracking
# when closing is 0, add the result in an auxiliary array and return
# if opening is 0, try to finish closing
# Call the usual backtracking function only when opening is greater than 0
# call the function for adding a closing bracket only when closing is greater than opening


def storeParen(opening, finalA, stringP, closing):
  if(closing == 0):
    finalA.append(stringP)
    return
  
  if(opening == 0):
    storeParen(opening, finalA, stringP + ')', closing-1)

  if(opening > 0):
    storeParen(opening-1, finalA, stringP+'(', closing)
    if(closing > opening):
      storeParen(opening, finalA, stringP+')', closing-1)

  
  

def generateParenthesis(n):
  A = []
  storeParen(n, A, "", n)
  print(A)
  
generateParenthesis(0)