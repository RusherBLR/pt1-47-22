"""Дан список стран и городов каждой страны. Затем даны названия городов.
 Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится
данный город."""


num_countr = int(input("Введите количество стран которое вы хотите добавить "))
counter_1 = 0
dictionary = {}

while counter_1 < num_countr:
    country = input("Введите сначало страну потом ее города через пробел ").split()
    dictionary[country[0]] = country[1:]
    counter_1 += 1

inquiry = int(input("сколько запросов будем делать? "))
counter_2 = 0

while counter_2 < inquiry:
    city = input("Введите название город: ")
    for (key, value) in dictionary.items():
        if city in value:
            print(f"город {city} находится в стране {key}")
    counter_2 += 1