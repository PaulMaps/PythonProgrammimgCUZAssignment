while True:
    user_input = input('enter any number of your choice')
    try:
        number = float(user_input)
        print('great you have entered a valid number ',number )
        break
    except ValueError:
        print('please enter a valid number:')
