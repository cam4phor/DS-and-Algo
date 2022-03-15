A = 23242

# Brute Force
# generate all possibilities 
# And find Product 
# if product exists 
# then we return false
# else return true


def IsColorFul(A):
    B = str(A)
    C = []
    for i in range(len(B)):
        for j in range(i+1, len(B)+1):
            num = B[i:j]
            prod = 1
            for k in range(len(num)):
                prod *= int(num[k])
            if(prod in C):
                return False
            else:
                C.append(prod)
    return True

print(IsColorFul(A))
