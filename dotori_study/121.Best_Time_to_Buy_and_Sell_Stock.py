# leet 121. Best Time to Buy and Sell Stock
# interview 12. 주식을 사고팔기 가장 좋은 시점
import sys

prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    profit = 0
    min_price = prices[0]
    for num in prices:
        if num < min_price:
            min_price = num
        elif num - min_price > profit:
            profit = num - min_price
    return profit


print(maxProfit(prices))