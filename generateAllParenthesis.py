'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.'''
def generateParenthesis(n):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2*n:
            ans.append(S)
            return
        if left < n:
            backtrack(S + '(',left+1, right)
        if right < left:
            backtrack(S + ')',left,right+1)
    backtrack()
    return ans
print generateParenthesis(3)
