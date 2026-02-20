"""
Programming Activity 1
Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""

colors = ["blue", "green", "red"]
for color in colors:
      print("color:", color)

"""
Programming Activity 2 
Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""

for color in colors:
      for letter in color:
            print("letter:", letter)
      print()

"""
Programming Activity 3
Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""

import random

random_numbers = []
for i in range(10):
      random_numbers.append(random.randint(1, 100))

print("random numbers:", random_numbers)
"""
Programming Activity 4 
Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""
count = 0
print(random_numbers)
for num in random_numbers:
    if count > 0:
      if random_numbers[count] % 2 == 0 and random_numbers[count - 1] % 2 == 0:
            print(random_numbers[count])
            print(random_numbers[count -1])
            print("two evens in a row")
    count += 1
"""
Programming Activity 5
1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""
file = open("/workspaces/Data_3500_Sandbox/stock_data/APPL.txt")
lines = file.readlines()
prices = []
for line in lines:
    prices.append(float(line))
total_avg = sum(prices) / len(prices)
print("total_avg:", total_avg)
five_day_avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
print("five_day_avg:", five_day_avg)
"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homweork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""
last_four_avg = sum(prices[-4:])/4
print("last_four_avg:", last_four_avg)
print()
i = 0
buy = 0
total_profit = 0
for price in prices:
    if i >= 4:
        avg = (prices[i] + prices[i - 1] + prices[i - 2] + prices[i - 3]) / 4
        if price < avg and buy == 0: 
            buy = price
            print("Buying at:", "\t", price)
        elif price > avg and buy != 0: 
            trade_profit = price - buy
            print("Selling at:", "\t", price)
            print("Trade profit:", "\t", trade_profit)
            total_profit += trade_profit
            buy = 0      
    i += 1 
print("total_profit:", "\t", total_profit)