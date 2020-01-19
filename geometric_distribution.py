numerator = 1
denumerator = 3
detect = 5
prob = numerator/denumerator
result = ((1-prob)**(detect-1))*prob
print("{:5.3f}".format(result))