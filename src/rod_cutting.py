def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): A list of prices for rod lengths from 1 to len(prices)
        n (int): The length of the rod to be cut
    
    Returns:
        int: Maximum obtainable value by cutting the rod
    
    Raises:
        ValueError: If input is invalid
    """
    # Validate inputs
    if not prices or n <= 0:
        return 0
    
    if len(prices) < n:
        # Pad prices list with zeros if needed
        prices = prices + [0] * (n - len(prices))
    
    # Initialize DP table
    dp = [0] * (n + 1)
    
    # Compute maximum value for each rod length
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j - 1] + dp[i - j])
        dp[i] = max_val
    
    return dp[n]