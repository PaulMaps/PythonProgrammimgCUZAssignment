def classify_number(number):
    number = int(number)
    if int(number) == 0:
        return 'zero'
    elif int(number) > 0:
        return 'positive'
    else:
        return 'negative'
    
while True:
    number = input('enter any integer of your choice: ')
    try:
        number = int(number)
        break
    except ValueError:
        print('invalid input, please input a valid number')

print(classify_number(number))