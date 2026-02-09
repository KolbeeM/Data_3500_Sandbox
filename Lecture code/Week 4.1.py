# # Maybe
# nums = [1, 2, 3, 4, 5]
# count = 0
# for num in nums:
#     avg = avg + num / 5
#     if num > avg:
#         count = count + 1

year = 1900

if year % 4 == 0:
    if year % 100 == 0:
        print("not a leap year")
    else:
        print("its a leap year!")
else:
    print("Not a leap year.")


import random
secret_num = random.randint(1, 100)

