""" Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
а также количество S товара. Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""


M = int(input("Enter the quantity of rubles "))
N = int(input("Enter the quantity of kopecks "))
print("item price", M, "rubles", N, "kopecks ")
S = int(input("Enter the quantity of item "))
print("quantity of item ", S)
price_kops = M * 100 + N
L = price_kops * S
x_rub = int(L / 100)
x_kop = L - x_rub * 100
print("total price", x_rub, "rubles", x_kop, "kopecks")
