def calculate_average(*numbers):
    '''
    this function calculates the average form the string of numbers entered by the user 

    params:
    it uses the args function to collect an undefined number of parameters from the users 

    output:
    it outputs the average of any numbers entered by the user which is calculated by sum divided by the total numbers
    '''
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
    

user_input = input('enter the numbers separated by spaces: ')

# change the string of numbers into an iterable list 

user_list = user_input.split()

# now add them as floats

try:
    numbers = [float(num) for num in user_list]
    print(calculate_average(*numbers))
except ValueError:
    print('one or more inputs you entered is invalid ') 