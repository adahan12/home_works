#Условные конструкции и Операторытсравнения, Циклы



# svetofor = 'off'
#
# if svetofor == 'green':
#     print('Go')
# elif svetofor == 'yellow' or 'red':
#     print('attention')
# else:
#     'look at situation'

# if 0:
#     print("этот обьект правда")

#and or not
a = 2 and 3
print(a)

#number = 100

cleaned_room = True
cooked_dinner = False
if cleaned_room or cooked_dinner:
    print("что-то сделано")


#
# while True:
#     guess = int(input('Введите число:'))
#     if number != guess:
#         print('не равно')
#     elif number == guess:
#         print('равно')
#         break
# # ==, <=, >=, !=
#
# for number in range(20):
#         if number % 2 == 0:
#             print(number)
#
#     print(10 > 2 and 10 > 9)      True
#     print(10 > 2 and 10 > 11 )  False?
#     print(10 > 2 or 10 > 11)    True
#     print(10 > 2 and not 10 > 11)True??
#     print(not(10 > 2 or 10 > 11)) Folse