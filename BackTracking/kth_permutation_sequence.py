import sys
import math

A = 4
B = 16
C = [ind + 1 for ind in range(A)]

print (C)
# algo:
    # get the number (n-1)!
    # calc: k/(n-1)! = T and k%(n-1)! = S
    # append into an array the Tth digit from the generated array and remove that from the array
    # repeat after taking S as K till we have 1 digit left in the array

n = A
X = []

while(n >= 1):
    print ("prev Rem = " + str(B))
    fact_num = math.factorial(n-1)
    print("fact = " + str(fact_num))
    print("array = " + str(C)) 
    T = B//fact_num
    print("div = " + str(T))
    S = B%fact_num
    print("rem = " + str(S))
    if S == 0:
        T -= 1
        S = fact_num
    X.append(C[T])
    print("appended elem = " + str(C[T]))
    print(" ")
    del C[T]
    B = S
    n -= 1
print(X)







