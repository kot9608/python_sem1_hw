# Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

m=int(input("Введите длинну шоколадки в дольках: "))
n=int(input("Введите ширину шоколадки в дольках: "))
k=int(input("Введите желаемый кусочек в дольках: "))
if k<n*m and (k%m==0 or k%n==0):
    print("Да, можно отломать желаемое количество долек")
else:
    print("Не получится(")