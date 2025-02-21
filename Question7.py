import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Step 2: Process the list
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers lower than 50 with "XX"
        random_numbers[i] = "XX"

# Step 3: Print the modified list
print(random_numbers)
