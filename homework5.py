my_list = ['apple', 'banana', 'meat', 'shugar', 'milk', 'baguette']
print('список продуктов: ', my_list)
print('Первый элемент: ', my_list[0], "Последний элемент: ", my_list[-1])
my_list.append('milk')
print('С 3 до 5: ',my_list[2:5])
print('Измененный список: ', my_list)

my_dict = {'apple':"Яблоко", 'meat':"Мясо", 'milk':"Молоко"}
print("Словарь: ", my_dict)
print("Вывод значения для заданного ключа: ", my_dict['apple'])
my_dict.update({'banana':'Банан'})
print("Измененный словарь: ", my_dict)
