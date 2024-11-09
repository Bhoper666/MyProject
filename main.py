my_list = []

numb_input = int(input('How many number you want? >>> '))

for i in range(numb_input):
    user_input = int(input('Enter number >>> '))
    my_list.append(user_input**2)

print(my_list)
