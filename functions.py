def print_fo(name, surname, patronymic):
    name_up = name.upper()[:1]
    surname_up = surname.upper()[:1]
    patronymic_up = patronymic.upper()[:1]
    print(name_up, surname_up, patronymic_up)


name = input('Type your name :')
surname = input('Type your surname:')
patronymic = input('Type your patronymic:')
print(print_fo(name, surname, patronymic))
