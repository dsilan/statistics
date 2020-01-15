import math
def solution(arr):
    l = len(arr)
    mean = sum(arr)/l
    print(mean) #mean
    arr.sort() #median
    if l%2 == 0: 
        print((arr[l//2-1]+arr[l//2])//2)
    else:
        print(arr[l//2])
    mod = arr[0] #mod
    cnt = 0
    for i in arr:
        countOfEl = arr.count(i)
        if countOfEl > cnt:
            cnt = countOfEl
            mod = i
    print(mod)
    summary = 0
    #standard deviation
    for x in arr:
        summary += (x - mean) ** 2
    ss = math.sqrt(summary / l )
    print(ss)
N = input()
str_arr = input().split(' ') #will take in a string of numbers separated by a space
ar = [int(num) for num in str_arr]
solution(ar)
