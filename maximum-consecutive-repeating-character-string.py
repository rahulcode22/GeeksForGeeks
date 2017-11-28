'''
Given a string, the task is to find maximum consecutive repeating character in string.

Note : We do not need to consider overall count, but the count of repeating that appear at one place.

Examples:

Input : str = "geeekk"
Output : e

Input : str = "aaaabbcbbb"
Output : a
'''
def maxConsecutiveRepeatingchar(string):
    n = len(string)
    dp = [0]*n
    dp[0] = 1
    for i in range(1,n):
        if string[i] == string[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    index = dp.index(max(dp))
    print string[index]
maxConsecutiveRepeatingchar(raw_input())
