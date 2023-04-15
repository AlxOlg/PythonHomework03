# Сколько раз встречается некоторое число в массиве.
N = int(input('Количество элементов массива: '))
import random
A = [random.randint(0, 10) for i in range(N)]
print(A)
X = int(input('Число для поиска и подсчета: '))
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
print(f'{count} раз')
