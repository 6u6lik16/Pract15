def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 2, 3)
print_params()
print_params(b=25)  # work
print_params(c=[1, 2, 3])  # work
values_list = ['Rapapapam', 322, False]  # Список
values_dict = {'a': 2, 'b': 'pam', 'c': True}  # Словарь
print_params(*values_list)  # Расспаковка списка
print_params(**values_dict)  # Расспаковка словаря
values_list_2 = ['pam', True]
print_params(*values_list_2, 42) # Расспаковка списка из 2 элементов
