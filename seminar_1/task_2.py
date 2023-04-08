# Найдите сумму цифр трехзначного числа. 
number = int (input ("Введите трехзначное число: "))
summ = 0
while number > 0:
    x = number%10
    summ = summ + x
    number = number//10
print (summ)