# variables

first_name = "lily"
last_name = "bell"
age = 365
is_it_monday = False
gas_price = 2.50

# can't do this

# ? = "hello"
# . = "hi"
# 2sday = "tuesday"
# str = "string"
# int = 56

aggieswintoday = True

# math

age = 21
print("age:", age)
age = age + 1
print("age:", age)
age = age - 1
print("age:", age)
age = age / 2
print("age:", age)
age = age * 2
print("age:", age)
age = age // 2
print("age:", age)
age = age % 2
print("age:", age)
age = age ** 2
print("age:", age)

# print function

# print()
# print("something new")
# print(age + first_name)

# triple quote strings

"""
2.3 description of the problem here. take all the variables, do all the math. solve all the problems.

maybe there is more description here. IDK. But you can add it all here and it will not output.
"""

menu = """
Pizza           $5
soda            $5
Fries           $6
Popcorn         $10
Popcorn Bucket  $30
"""
print(menu)

"""
Adam is running a half marathon. His avg mile time is 5:55.
for the half (13.1), What is his projected finish time?
Output the result in this format:
"time: hr:min:sec"
"""
minute = 5
sec = 55
pace_seconds = sec + (minute * 60)
print("pace in seconds: ", pace_seconds)

total_half_sec = pace_seconds * 13.1
print("total time in seconds for the half: ", total_half_sec)

projected_hours = total_half_sec // 3600
print(projected_hours)

projected_minutes = (total_half_sec % 3600) // 60
print(projected_minutes)

projected_seconds = total_half_sec % 60
print(projected_seconds)

print("Your marathon time:", int(projected_hours), ":", int(projected_minutes), ":", projected_seconds)