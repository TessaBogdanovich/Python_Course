# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, 
# которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

n = input("Введите количество монеток: ")
x = 0
y = 0
for i in range(len(n)):
    if int(n[i]) == 1:
     x+=1
    elif int(n[i]) == 0:
        y+=1
if x<y:
    print(f"Перевернуть {x} орлов")
else:
    print(f"Перевернуть {y} решек")
