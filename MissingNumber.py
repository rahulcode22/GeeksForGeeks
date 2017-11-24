#Approach 1 Simple One
def missing(arr, n):
    temp = [i for i in range(1,n+1)]
    for i in temp:
        if i not in arr:
            print i

arr = [1,2,3,3,5]
missing(arr, 5)

#Approach 2
#Sum Approach
def missing(arr, n):
    sum_expected = (n*(n+1))/2
    sum_actual = sum(arr)
    return sum_expected - sum_actual

#Approach 3
#Xor Approach
def missing(arr, n):
    xor1 = arr[0]
    xor2 = 1
    for i in range(1,n):
        xor1 = xor1^arr[i]
    for i in range(2,n+2):
        x2 = x2^i

    return xor1^xor2
