# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# Последняя строка содержит число X


n = int(input('Введите размер элементов списка: '))
list_n = input('Введите элементы списка через пробел: ').split()
x = input("Введите число, которое нужно найти: ")
print(list_n.count(x))

