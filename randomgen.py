import random

# Function with input of user that draws amount of random numbers user defines.
def random_cal():
    int = 0
    list = []
    while int < 5:
        random_numb = random.randint(1, 6)
        list.append(random_numb)
        int += 1
    return list
