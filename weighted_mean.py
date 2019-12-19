N = input()
str_Notes = input().split(' ')
Notes = [int(num) for num in str_Notes]
str_Weights = input().split(' ')
Weights = [int(num) for num in str_Weights]

for i in range(0,int(N)):
    Notes[i] = Notes[i] * Weights[i]
print(round(sum(Notes)/sum(Weights), 1))