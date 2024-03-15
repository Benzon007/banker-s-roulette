import random
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
a=len(names)
b=random.randint(0,a-1)
print(f"{names[b]} is going to buy the meal today!")
