class NegativeNumberError(Exception):
    '''its the one that is raised when the input is negative'''
    pass

def check_positive(number):
     if number < 0:
          raise NegativeNumberError('negative numbers are not allowed')
     else:
          print(f'the number {number} is positve ', number)

while True:
    user_input = input('enter any positive number')
    try:
        number = float(user_input)
        check_positive(number)
        break
    except ValueError:
         print('please enter a valid number')
    except NegativeNumberError as e:
         print('custom exception caught', e)