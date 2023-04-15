# Найти в массиве самый близкий по величине элемент к заданному числу.
N = int(input('Количество элементов массива: '))
import random
A = [random.randint(0, 10) for i in range(N)]
print(A)
X = int(input('Число для поиска: '))
# Результат - первый по счету элемент из возможного множества.
index = 0
for i in range(N):
    if abs(A[i] - X) < abs(A[index] - X):
        index = i
print(f'{A[index]} - самое близкое по величине')
