'''
Given two strings str1 and str2, find if str1 is a subsequence of str2. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements (source: wiki). Expected time complexity is linear.
'''
#REcursive solution
def isSubsequence(s1, s2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
    if s1[m-1] == s2[n-1]:
        return isSubsequence(s1, s2, m-1, n-1)
    return isSubsequence(s1,s2,m,n-1)

s1 = "rahul"
s2 = "driashwaulri"
m = len(s1)
n = len(s2)
if isSubsequence(s1, s2, m, n):
    print "True"
else:
    print "False"
