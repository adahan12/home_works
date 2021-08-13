# Условие конструкции и операторы сравнения , Циклы

# counter = 0
#
# while counter < 10:
# counter += 1
# print(counter)

cash = 1000000000000000000000000000

cash = cash + 10  # cash += 10
# cash -= 10
# cash /= 10


# truediv
a = 10
print(a / 2)

# moddiv
b = 11
b //= 2
print(b // 3)

number = 100
guess = int(input('какое то число'))

if number != guess:
    print('не правильно')

if number >= guess:
    print('боольше или равно')

elif number == guess:
    print('равно')
else:
    print('введите правильное  число')
