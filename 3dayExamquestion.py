lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prices = []
for list in lst:
    prices.append(float(list))
for i in range(len(prices) - 2):
    three_day_avg = (prices[i] + prices[i+1] + prices[i+2]) / 3
    print("three_day_avg:", three_day_avg)
