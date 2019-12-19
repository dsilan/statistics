def getMedian(ary):
    l= len(ary)
    if l%2 == 0: 
        return (ary[l//2-1]+ary[l//2])//2
    else:
        return ary[l//2]

n = 9
mid = n // 2
Q1, Q2, Q3 = 0, 0, 0 #lower, median, upper
arr = [3, 7, 8, 5, 12, 14, 21, 13, 18]
#3 5 7 8 12 13 14 18 21
arr.sort()

Q2 = getMedian(arr)
Q1 = getMedian(arr[:mid])
#upper is different if n is even or odd
if n%2 == 0: 
    Q3 = getMedian(arr[mid:])
else:
    Q3 = getMedian(arr[mid+1:])

print(Q1, Q2, Q3)
