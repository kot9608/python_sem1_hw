# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

chislo_3z=int(input("Введите трёхзначное число: "))
print('Введённое число:', chislo_3z)
sum=int(0)

print('chislo_3z//10', chislo_3z//10)

while chislo_3z>9:
     sum=sum+chislo_3z%10
#     print(chislo_3z)
     chislo_3z=chislo_3z//10
# print(sum)
print ('Сумма цифр в числе =', sum+chislo_3z%10)