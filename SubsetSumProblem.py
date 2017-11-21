#Complexity O(sum*n)
def isSubsetSum(arr,n,sum_):
    subset = [[True]*(sum_+1)]*(n+1)
    #If sum is 0, then answer is True
    for i in range(n+1):
        subset[i][0] = True

    #If sum is not 0 and set is empty,
    #then answer is False
    for i in range(1,sum_+1):
        subset[0][i] = False

    for i in range(1,n+1):
        for j in range(1,sum_+1):
            if j < st[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= st[i-1]:
                subset[i][j] = subset[i-1][j] or subset[i-1][j-st[i-1]]
    return subset[n][sum_]

st = [1,2,3]
sum_ = 7
n = len(st)
print isSubsetSum(st,n,sum_)
