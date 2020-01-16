def fact(n):
    return 1 if n == 0 else n*fact(n-1)
def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))
def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)
per, n = list(map(float, input().split(" ")))
p = per/100
prob = round(sum([b(i,n, p) for i in range(0, 3)]), 3)
prob2 = round(sum([b(i,n, p) for i in range(2, 11)]), 3)
print(prob)
print(prob2)