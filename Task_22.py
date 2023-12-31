# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множеста: "))
m = int(input("Введите количество элементов второго множеста: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества: ")
for i in range(n):
    element1 = int(input())
    set1.add(element1)

print("Введите элементы второго множества: ")

for j in range(m):
    element2 = int(input())
    set2.add(element2)

common_elements = sorted(set1.intersection(set2))

print("Общие элементы без повторений:", common_elements)