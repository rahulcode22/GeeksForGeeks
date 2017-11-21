'''
 You have an array of integers. Find the first pair of integers whose sum is equal to k.
'''
def checkpair(arr,k):
    arr.sort()
    n = len(arr)
    l = 0
    r = n-1
    while l < r:
        if arr[l] + arr[r] == k:
            return arr[l],arr[r]
        elif arr[l] + arr[r] > k:
            r -= 1
        else:
            l += 1
    return -1

#HASHMAP Approach
CONST_MAX = 100000
def checkpair(arr,k):
    n = len(arr)
    #Intialize hash map as 0
    binmap = [0]*CONST_MAX

    for i in range(n):
        temp = k - arr[i]
        if temp >= 0 and binmap[temp] == 1:
            print arr[i], temp
        binmap[arr[i]] = 1
