# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Количество дней - целое число

# Input:
# n = 700
# m = 750
# Output:
# 1


n = int(input()) #700 - скорость
m = int(input()) #750 - расстояние
print((n+m-1)//n) #1449//700 n+m-1 Прибавление (скорости-1) - добавляем число, которое максимально приближено, но не кратно скорости. 
# Чтобы мы расстояние кратное скорости проезжали за полное количество дней, а если оно больше или меньше- на количество полных дней+1