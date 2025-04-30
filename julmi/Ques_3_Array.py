############################################### Question #########################################################

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

############################################### Solution In Python ##################################################

#Solution 1
def maxProfit(prices):
    min_price = float('inf')  # Initialize to infinity
    max_profit = 0  # Initialize maximum profit to 0

    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate the profit if sold at the current price and update max profit
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

print(maxProfit([7, 2, 5, 3, 6, 4]))  # Output: 5
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0

#Solution 2
def maxProfit(prices):
    min_price = float('inf')
    max_profit = float('-inf')

    for j in range(len(prices)):
        for i in range(j,len(prices)):
            if prices[i] - prices[j] > max_profit:
                max_profit = prices[i] - prices[j]
    return max_profit


max_profit = maxProfit([7, 1, 5, 3, 6, 4])
print(max_profit)
max_profit01 = maxProfit([7,6,4,3,1])  # 5  
print(max_profit01) # 0    