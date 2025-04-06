import random

random_numbers = [random.randint(1,100) for i in range(10)]

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers)