import math
result = 0
def fact(r):
    return 1 if r == 0 else r*fact(r-1)

#This func is for dist like P(r <= 3, l = 5)
def poisson(r,l, result):
    if r >= 0:
        result += (l**r)*(1/(math.e**l))/fact(r)
        return poisson(r-1, l, result)
    else:
        return result
print("{:5.3f}".format(poisson(3,5, result)))

r, l = 3, 2
#This is basic dist like P(k = 3, l= 2)
print((l**r)*(1/(math.e**l))/fact(r))