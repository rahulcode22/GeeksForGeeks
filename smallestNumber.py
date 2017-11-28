'''
 Given a sequence of M and N with M representing increasing and N representing decreasing, output the smallest number that follows this pattern.

Input    : MMMM
Output   : 12345

Input    : NNNN
Output   : 54321

Input    : MMNM
Output   : 2314
'''
def printMinimumNumber(arr):
    n = len(arr)
    min_no = 1
    index_I = 0
    ans = []
    if arr[0] == 'I':
        ans.append(1)
        ans.append(2)
        min_no = 3
        index_I =1
    elif arr[0] == 'M':
        ans.append(2)
        ans.append(1)
        min_no = 3
        index_I = 0

    for i in range(1,n):
        if arr[i] == 'I':
            ans.append(min_no)
            min_no += 1
            index_I = i+1
        else:
            ans.append(ans[i])
            for j in range(index_I,i+1):
                ans[j] += 1
            min_no += 1
    for i in range(len(ans)):
        print ans[i]
printMinimumNumber("IDID")
