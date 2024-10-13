# You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# brute force

def stock(prices):
    if prices == sorted(prices):
        return prices[len(prices) - 1] - prices[0]
        
    if prices == sorted(prices, reverse = True):
        return 0

    rev = prices[::-1]
    sums = []
    
    # sample rev | [4, 6, 3, 5, 1, 7]
    for j in range(len(rev)):
        for k in range(j, len(rev)):
            sums.append(rev[j] - rev[k])
        if len(sums) % len(rev) == 0:
            rev == rev[1:]
            
    return max(sums)

# better solution

def stock2(prices):
    buy = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy

    return profit