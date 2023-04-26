# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную
# возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

list  = [1, 5, 2, 3, 4, 6, 1, 7]
list2 = []
def importlist2(list, list2):
    a = random.randint(1, (len(list)-1))
    b = list[a]
    list2.append(b)
    c = random.randint(a, (len(list)-1))
    f = random.randint(c, (len(list)-1))
    d = list[c: f]
    for x in d:
        if x > list2[-1]:
            list2.append(x)
importlist2(list, list2)
while len(list2) < 2:
    list2.clear()
    importlist2(list, list2)



print(list)
print(list2)


