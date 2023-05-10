def weighted_interval_scheduling(intervals, weights):
    # Sort the intervals by end time
    intervals = sorted(intervals, key=lambda x: x[1])

    # Initialize the DP table with zeros
    dp = [0] * (len(intervals) + 1)

    # Iterate over the intervals in reverse order
    for i in range(len(intervals) - 1, -1, -1):
        # Find the latest interval that doesn't overlap with the current one
        j = i + 1
        while j < len(intervals) and intervals[j][0] < intervals[i][1]:
            j += 1

        # Compute the maximum weight that can be obtained by considering the current interval
        # and the maximum weight that can be obtained by skipping it
        weight_with_interval = weights[i] + dp[j]
        weight_without_interval = dp[i + 1]

        # Choose the maximum weight and store it in the DP table
        dp[i] = max(weight_with_interval, weight_without_interval)

    # Return the maximum weight
    return dp[0]
intervals = [(0, 3), (2, 4), (3, 5), (4, 7), (5, 8), (7, 9)]
weights = [2, 3, 4, 5, 6, 7]

max_weight = weighted_interval_scheduling(intervals, weights)
print("Maximum weight:", max_weight)
