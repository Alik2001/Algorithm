def knapSack(W, wt, val, n, memo):
    if n == 0 or W == 0:
        return 0

    if memo[n][W] != -1: 
        return memo[n][W]

    if wt[n - 1] > W:
        memo[n][W] = knapSack(W, wt, val, n - 1, memo)
        return memo[n][W]
    else:
        memo[n][W] = max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1, memo),
                         knapSack(W, wt, val, n - 1, memo))
        return memo[n][W]

if __name__ == '__main__':
    profit = [30, 40, 60]
    weight = [3, 2, 5]
    W = 6
    n = len(profit)
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]  
    print(knapSack(W, weight, profit, n, memo))
