def knapsack_01(weights, values, capacity):
    n = len(weights)
    # Initialize the DP table with zeros
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If the item can fit in the knapsack, choose the maximum value between
            # taking the item and not taking it
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
            # If the item cannot fit in the knapsack, do not take it
            else:
                dp[i][j] = dp[i-1][j]

    # Return the maximum value
    return dp[n][capacity]
weights = [1, 2, 3, 4, 5]
values = [10, 20, 30, 40, 50]
capacity = 7

max_value = knapsack_01(weights, values, capacity)
print("Maximum value:", max_value)
