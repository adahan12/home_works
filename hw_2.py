# infinite cycle
while True:
    print(
        "для вывода всех медалистов введите: все\nдля вывода золотых медалистов введите: золото "
        "\nдля вывода серебрянных медалистов введите: серебро \nдля вывода бронзовых медалистов введите: бронза\n"
        "выйти: выйти")
    # data
    gold = []
    silver = ["Akjol", "Aisulu"]
    bronze = ["Aiperi"]
    request = input(":>")
    # выход
    if request == "выйти":
        break
    # если он хочет получить медалистов
    elif request == "все":
        print(gold + silver + bronze)
    elif request == "золото":
        print(gold)
    elif request == "серебро":
        print(silver)
    elif request == "бронза":
        print(bronze)
    # Оповестить пользователя при неправильном вводе и продолжать цикл.
    else:
        print("Неправильный ввод!")


