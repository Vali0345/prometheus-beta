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
    
    # Ensure prices list is long enough
    extended_prices = prices + [0] * (n - len(prices))
    
    # Initialize DP table
    dp = [0] * (n + 1)
    
    # Compute maximum value for each rod length
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            # Check the extended prices to handle all rod lengths
            current_val = extended_prices[j - 1] + dp[i - j]
            max_val = max(max_val, current_val)
        dp[i] = max_val
    
    return dp[n]