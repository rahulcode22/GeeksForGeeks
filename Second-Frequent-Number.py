'''
Print second frequently occurring number in given series
'''
def secondFrequent(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] == 2:
            return i

arr = [1,1,2,3,1,2,4]
print secondFrequent(arr)
