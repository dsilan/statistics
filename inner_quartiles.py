def getMedian(ary):
    l= len(ary)
    if l%2 == 0: 
        return (ary[l//2-1]+ary[l//2])//2
    else:
        return ary[l//2]

Q1, Q2, Q3 = 0, 0, 0 #lower, median, upper

N = input()
n = int(N)
str_arr = input().split(' ')
arr = [int(num) for num in str_arr]
str_frequences = input().split(' ')
frequences = [int(num) for num in str_frequences]

for i in range(0, n):
    for j in range(1, frequences[i]):
        arr.append(arr[i])
arr.sort()
mid = len(arr)//2
Q2 = getMedian(arr)
Q1 = getMedian(arr[:mid])
#upper is different if n is even or odd
if n%2 == 0: 
    Q3 = getMedian(arr[mid:])
else:
    Q3 = getMedian(arr[mid+1:])

print("iq= {0:.1f}".format(Q3-Q1))