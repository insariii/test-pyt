# Оценка сложности алгоритма Bucket Sort

# Алгоритм Bucket Sort имеет следующую вычислительную сложность:
# Лучший случай: O(n + k)
# Средний случай: O(n + k)
# Худший случай: O(n^2)

# где:
# n — количество элементов
# k — количество ведер


# Набросок доказательства

# 1. Распределение элементов по ведрам
# Алгоритм проходит по всем элементам массива и распределяет их по ведрам
# Сложность: O(n)


# 2. Сортировка элементов внутри ведер

# Если элементы распределены равномерно:
# - в каждом ведре примерно одинаковое количество элементов
# - сортировка выполняется быстро
# Итог: O(n)

# Если элементы распределены неравномерно:
# - большинство элементов попадает в одно ведро
# - фактически сортируется почти весь массив
# Итог: O(n^2)


# 3. Сборка результата
# После сортировки элементы объединяются обратно
# Сложность: O(n)


# Итоговая сложность:
# O(n) + O(n) + O(n) = O(n)

# В среднем случае: O(n + k)
# В худшем случае: O(n^2)


# Вывод:
# Bucket Sort имеет линейную сложность O(n) при равномерном распределении данных.
# В худшем случае сложность возрастает до O(n^2).

import os
import time as t
import numpy as np
import matplotlib.pyplot as plt


# ==============================
# ОЦЕНКА СЛОЖНОСТИ (ТЕОРИЯ)
# ==============================

# Алгоритм Bucket Sort имеет сложность:
# Лучший случай: O(n + k)
# Средний случай: O(n + k)
# Худший случай: O(n^2)

# где:
# n — количество элементов
# k — количество ведер

# Доказательство (набросок):
# 1. Распределение элементов: O(n)
# 2. Сортировка ведер:
#    - равномерно → O(n)
#    - неравномерно → O(n^2)
# 3. Сборка: O(n)


# ==============================
# АЛГОРИТМ
# ==============================

def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0

    min_val = min(arr)
    max_val = max(arr)

    buckets = [[] for _ in range(n)]
    iterations = 0

    for num in arr:
        index = min(n - 1,
                    int((num - min_val) / (max_val - min_val + 1e-9) * n))
        buckets[index].append(num)
        iterations += 1

    for i in range(n):
        buckets[i].sort()
        iterations += len(buckets[i])

    result = []
    for bucket in buckets:
        result.extend(bucket)
        iterations += len(bucket)

    return result, iterations


# ==============================
# ЗАМЕРЫ
# ==============================

def measure(func, arr):
    start = t.perf_counter()
    _, iterations = func(arr.copy())
    end = t.perf_counter()
    return end - start, iterations


# ==============================
# ГЕНЕРАЦИЯ ДАННЫХ
# ==============================

sizes = [10, 50, 100, 200, 500, 1000]

times = []
iters = []

for size in sizes:
    data = np.random.randint(1, 100, size=size)
    time_val, iter_val = measure(bucket_sort, data)

    times.append(time_val)
    iters.append(iter_val)


# ==============================
# ГРАФИКИ ПРАКТИКИ
# ==============================

# Время
plt.figure()
plt.plot(sizes, times, marker='o')
plt.title("Время выполнения Bucket Sort")
plt.xlabel("Размер массива")
plt.ylabel("Время")
plt.grid()
plt.show()

# Итерации
plt.figure()
plt.plot(sizes, iters, marker='o')
plt.title("Количество операций")
plt.xlabel("Размер массива")
plt.ylabel("Итерации")
plt.grid()
plt.show()


# ==============================
# ТЕОРЕТИЧЕСКИЙ ГРАФИК
# ==============================

n = np.linspace(1, 1000, 100)

plt.figure()
plt.plot(n, n, label="O(n)")
plt.plot(n, n**2, label="O(n^2)")
plt.title("Теоретическая сложность")
plt.legend()
plt.grid()
plt.show()


# ==============================
# СРАВНЕНИЕ
# ==============================

times_norm = np.array(times) / max(times)
sizes_norm = np.array(sizes) / max(sizes)

plt.figure()
plt.plot(sizes, times_norm, marker='o', label="Практика")
plt.plot(sizes, sizes_norm, label="O(n)")
plt.title("Сравнение теории и практики")
plt.legend()
plt.grid()
plt.show()


# ==============================
# ВЫВОД
# ==============================

# Теоретически Bucket Sort имеет сложность O(n).
# Практические результаты подтверждают это,
# однако есть отклонения.

# Причины:
# 1. Неравномерное распределение данных
# 2. Встроенная сортировка (O(n log n))
# 3. Накладные расходы Python
