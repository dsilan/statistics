numerator = 1
denumerator = 3
detect = 5
prob = numerator/denumerator
result = ((1-prob)**(detect-1))*prob
print("{:5.3f}".format(result))

"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the  defect is found during the 5th inspection?
"""