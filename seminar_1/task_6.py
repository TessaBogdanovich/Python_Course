# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

ticket_number = input ("Введите номер билета: ")
print(type (ticket_number))
print(ticket_number[:3])
number_1 = int (ticket_number[:3])
summ1 = 0
while number_1 > 0:
    x = number_1%10
    summ1 = summ1 + x
    number_1 = number_1//10
print (summ1)

print(ticket_number[3:])
number_2 = int (ticket_number[3:])
summ2 = 0
while number_2 > 0:
    x = number_2%10
    summ2 = summ2 + x
    number_2 = number_2//10
print (summ2)

if summ1 == summ2:
    print("Yes")
else:
    print("No")
