numbers = [10, 15, 3, 7]
k = 17 

def target_num(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print("found", target, "in number list")
                break


colors = ["purple", "green", "blue"]
print("colors:", colors)
colors.append("yellow")
print("colors:", colors)
colors.pop(1)
print("colors:", colors)

colors.insert(0, "pink")
print("colors:", colors)


#searching/slicing and sorting lists.

i = 0

for i in range(len(colors)):
    print("colors:", colors[i])

for color in colors:
    print("color:", color)

print(colors[0:2])



#figure out of two words are anagrams of each other
def anagram(word1, word2):
    word1_list = []
    word2_list = []
    if len(word1) == len(word2):
        for letter in word1:
            word1_list.append(letter)
        for letter in word2:
            word2_list.append(letter)
    return False

if anagram("listen", "silent"):
    print("the words are anagrams")
else:
    print("the words are not anagrams")