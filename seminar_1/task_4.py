# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
#  журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

S = int (input ("Введите сумму: "))
Serge = S // 3 //2
Petr = Serge
print (f"Журавлики Сергея {Serge} и Журавлики Петра {Petr}")
Kate = (Serge + Petr) * 2
print(f"Журавлики Кати {Kate}")