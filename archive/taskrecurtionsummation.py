"""
Напишите рекурсивную функцию summation(n), 
которая будет принимать положительное целое число n
 и возвращать сумму чисел от 1 до n.
"""
number = int(input("Введите число:"))

def Summation(num):
    if num == 1:
        return 1
    else:
        return num + Summation(num-1)
    

print(Summation(number))
        