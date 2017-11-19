#Complexity O(nW)
def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j < wt[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
    return dp[n][W]
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapsack(W, wt, val, n)
