# Dynamic types
x = 1
x = "aggie basketball"
x = True

print(type(x))

#input
age = int(input("Please enter your age: "))
print(type(age))

print("on your next birthday you will be", age + 1)

#casting
# int()
# str()
# float()
# bool()
# eval()# tries to figure out the best type

# if

age = 12

if age > 20:
    print("The twenties are the best years of your life")
if age >= 13: # false
    print("You are a teenager. Have fun :)")
else:
    print("you are still a child :)")


if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else: 
    print("child")

# hurd premium

student = input("are you a current usu student: (Y/N)")
hurdP = input("Do you have Hurd premium: (Y/N)")

if student == "Y":
    print("you get into the game free!")
if hurdP == "Y":
    print("you get into the game 15 minutes early!")
else:
    print("you need to buy a ticket. they're not too expensive") 
# min, max, range

grades = [89, 56,100, 100, 90, 0, 5]

print("min:", min(grades))
print("max:", max(grades))

print(range(10))