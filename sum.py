#Напишите программу, которая считывает со стандартного ввода целые числа,
#по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

chek = int(input())
sum = 0
while chek != 0:
  sum+=chek
  chek = int(input())
print(sum)

