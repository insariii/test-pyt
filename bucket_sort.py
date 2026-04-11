import time as t
import numpy as np
import os
import matplotlib.pyplot as plt

REPEATS = 5

def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0

    min_val = min(arr)
    max_val = max(arr)

    bucket_count = n
    buckets = [[] for _ in range(bucket_count)]
    iterations = 0  # счётчик итераций

    # Распределение элементов по корзинам
    for num in arr:
        iterations += 1
        # Вычисляем индекс корзины для текущего элемента
        index = min(
            bucket_count - 1,
            int((num - min_val) / (max_val - min_val + 1e-9) * bucket_count)
        )
        # Добавляем элемент в соответствующую корзину
        buckets[index].append(num)

    # Сортировка каждой корзины
    for i in range(bucket_count):
        if buckets[i]:  # если корзина не пустая
            buckets[i].sort()
            iterations += len(buckets[i])  # учитываем итерации сортировки

    # Сборка отсортированного массива
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result, iterations

def measure_time(func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        test_arr = arr.copy()
        start = t.perf_counter()
        func(test_arr)
        end = t.perf_counter()
        times.append(end - start)
    return np.mean(times)

def measure_iterations(func, arr, repeats=5):
    iterations = []
    for _ in range(repeats):
        test_arr = arr.copy()
        _, iter_count = func(test_arr)  # получаем количество итераций
        iterations.append(iter_count)
    return np.mean(iterations)

# Создаём тестовый массив один раз
arr_np = np.random.randint(1, 101, size=30)

print(f'{measure_time(bucket_sort, arr_np):.5f}')

# СЧИТЫВАНИЕ ДАННЫХ
data_dir = "data"  # папка с файлами
num_files = len(os.listdir(data_dir))  # получаем кол-во файлов

def read_dataset(filepath):
    """
    Считывает набор чисел из текстового файла.

    Каждый элемент файла должен быть на отдельной строке.

    Параметры:
        filepath (str): путь к файлу с числами.

    Возвращает:
        list[int]: список чисел из файла.
    """
    numbers = []  # создаём пустой список для чисел
    with open(filepath, 'r') as file:  # открываем файл на чтение
        for line in file:  # проходим по каждой строке в файле
            # Каждая строка файла — это текст (строка).
            # Метод strip() убирает пробелы и символ переноса строки '\n'.
            # int(...) преобразует текст в число, чтобы с ним можно было выполнять математические операции.
            numbers.append(int(line.strip()))
    return numbers  # возвращаем список чисел

result = {}

# Перебираем файлы по порядку
for i in range(1, num_files + 1):
    # Формируем имя файла (например: data_1.txt и тд)
    filename = f"data_{i}.txt"

    # Формируем полный путь к файлу
    filepath = os.path.join(data_dir, filename)

    # Считываем данные
    try:
        data = read_dataset(filepath)
    except FileNotFoundError:
        print('Файл не найден')
        continue

    size = len(data)
    mean_time = measure_time(bucket_sort, data)
    mean_iter = measure_iterations(bucket_sort, data)
    result[size] = (mean_time, mean_iter)
    # выводим имя файла, размер набора и первые 10 элементов для проверки
    print(f"{filename}: размер {len(data)}, первые 10 чисел: {data[:10]}")

with open('bucket_results.txt', 'w') as f:
    for size, (time_val, iter_val) in result.items():
        # Преобразуем значения в обычные float и int, чтобы избежать np.float64
        f.write(f"{size} {time_val:.8f} {int(iter_val)}\n")

print("Результаты сохранены в bucket_results.txt")

sizes = []
times = []
iterations = []
with open('bucket_results.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            continue
        try:
            sizes.append(int(parts[0]))
            times.append(float(parts[1]))
            iterations.append(int(parts[2]))
        except ValueError:
            continue

# График времени выполнения
plt.figure(figsize=(15, 8))
plt.plot(sizes, times, marker='o', label="Bucket Sort")
plt.xlabel("Размер данных")
plt.ylabel("Среднее время выполнения (сек)")
plt.title("Зависимость времени выполнения от размера данных")
plt.legend()
plt.grid(True)
plt.savefig('plot.png')
plt.show()

# График количества итераций
plt.figure(figsize=(15, 8))
plt.plot(sizes, iterations, marker='s', color='red', label="Итерации")
plt.xlabel("Размер данных")
plt.ylabel("Среднее количество итераций")
plt.title("Зависимость количества итераций от размера данных")
plt.legend()
plt.grid(True)
plt.savefig('iterations_plot.png')
plt.show()

sizes = np.array(sizes)
# Теоретическая сложность
theoretical = sizes  # Bucket Sort в лучшем случае O(n)

# Нормируем для сравнения (подбираем масштаб)
scale_factor_time = max(times) / max(theoretical)
theoretical_time = theoretical * scale_factor_time

plt.figure(figsize=(15, 8))
plt.plot(sizes, times, 'o-', label='Экспериментальные данные')
plt.plot(sizes, theoretical_time, '--', label='Теоретическая O(n)')
plt.xlabel("Размер данных")
plt.ylabel("Время (сек)")
plt.title("Сравнение экспериментальных данных с теоретической моделью O(n)")
plt.legend()
plt.grid(True)
plt.show()

"""
Оценка временной сложности Bucket Sort:

Лучший случай: O(n + k), где k — количество корзин.
Когда данные равномерно распределены, каждая корзина содержит мало элементов,
и сортировка внутри корзин выполняется за O(1) на элемент.

Средний случай: O(n) при равномерном распределении данных.

Худший случай: O(n²) когда все элементы попадают в одну корзину.
В этом случае алгоритм сводится к обычной сортировке внутри одной корзины.

Факторы, влияющие на производительность:
- Распределение данных: равномерное распределение даёт лучший результат.
- Количество корзин: оптимально выбирать равное размеру массива.
- Диапазон значений: чем меньше диапазон, тем эффективнее сортировка.
"""
