data = ["O!", 705, "Megacom", 550, "Beeline", 770]

names = []
code = []

# Пройтись по списку data, добавить имена компаний в names и коды в code
for el in data:
    if type(el) == int:
        code.append(el)
    elif type(el) == str:
        names.append(el)

print(names)  # ['O!', 'Megacom', 'Beeline']
print(code)  # [705, 550, 770]

# Преобразовать списки names и code в кортеж
names = tuple(names)
code = tuple(code)
print(type(names))  # <class 'tuple'>

# Создать словарь my_dict на основе кортежей names и codes с помощью функции zip()
my_dict = dict(zip(names, code))
print(my_dict)  # {'O!': 705, 'Megacom': 550, 'Beeline': 770}

# Добавить к Ошке, Меге и Билайну коды, которые вы знаете
my_dict["O!"] = [my_dict["O!"], 703, 500]
my_dict["Megacom"] = [my_dict["Megacom"], 999]
my_dict["Beeline"] = [my_dict["Beeline"], 222]

print(my_dict) # (пример) {'O!': [705, 703, 500], 'Megacom': [550, 999], 'Beeline': [770, 222]}
