detect = 5
prob = 1/3
result = 0
def inspection(result, detect):
    result += ((1-prob)**(detect-1))
    print(result)
    if detect > 1:
        return inspection(result, detect-1)
    else:
        return result

result = inspection(result, detect)
print("{:5.3f}".format(result*prob))

"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the  defect is found during the first 5 inspection?
"""

"""
(2/3**4 + 2/3**3 + 2/3**2 + 2/3**1)*1/3
"""