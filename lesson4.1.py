# Структуры данных: Кортеж.

names = []
numbers = []

lst = [20,50,100,'Тоголок Молдо', 'Курманжан Датка', 'Токтогул сатылганов',]
lst.append('Алыкул Осмонов')
lst.append(200)
print(lst)

for i in lst:
    if type(i) == str:
        names.append(i)
    elif type(i) == int:
        numbers.append(i)

print(names)
print(numbers)

lst_tuple = tuple(lst)

print(type(lst_tuple))
print(list(zip(names, numbers)))
my_dict = dict(zip(names, numbers))
print(my_dict)
print("Программа завершена")
