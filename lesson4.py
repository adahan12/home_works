#Структуры данных: Словари (родолжение), кортежи.

student = {
    'name' : 'Adilet',
    'age' : 18,
    'height' : 1.80,
    'physic passed' : False,
}


if not student['height'] >= 1.80 and not student['physic passed']:
    print('ok', student['name'], "не прошел")
else:
    print('ok', student['name'], "Куттуктайм сени, аскер")