import random
import time

from avl_tree import AVLTree


tree = AVLTree()
root = None

data = [random.randint(1, 100000) for _ in range(10000)]

insert_times = []
insert_operations = []

search_times = []
search_operations = []

delete_times = []
delete_operations = []


# ДОБАВЛЕНИЕ

for number in data:
    tree.operations = 0

    start = time.perf_counter()

    root = tree.insert(root, number)

    end = time.perf_counter()

    insert_times.append(end - start)
    insert_operations.append(tree.operations)


# ПОИСК

search_elements = random.sample(data, 100)

for number in search_elements:
    tree.operations = 0

    start = time.perf_counter()

    tree.search(root, number)

    end = time.perf_counter()

    search_times.append(end - start)
    search_operations.append(tree.operations)


# УДАЛЕНИЕ

delete_elements = random.sample(data, 1000)

for number in delete_elements:
    tree.operations = 0

    start = time.perf_counter()

    root = tree.delete(root, number)

    end = time.perf_counter()

    delete_times.append(end - start)
    delete_operations.append(tree.operations)


# СРЕДНИЕ ЗНАЧЕНИЯ

avg_insert_time = sum(insert_times) / len(insert_times)
avg_insert_ops = sum(insert_operations) / len(insert_operations)

avg_search_time = sum(search_times) / len(search_times)
avg_search_ops = sum(search_operations) / len(search_operations)

avg_delete_time = sum(delete_times) / len(delete_times)
avg_delete_ops = sum(delete_operations) / len(delete_operations)


# ВЫВОД В КОНСОЛЬ

print("Добавление:")
print(avg_insert_time)
print(avg_insert_ops)

print("\nПоиск:")
print(avg_search_time)
print(avg_search_ops)

print("\nУдаление:")
print(avg_delete_time)
print(avg_delete_ops)


# СОХРАНЕНИЕ В ФАЙЛ

with open("results.txt", "w", encoding="utf-8") as file:
    file.write("СРЕДНИЕ РЕЗУЛЬТАТЫ\n\n")

    file.write("Добавление\n")
    file.write(f"Среднее время: {avg_insert_time}\n")
    file.write(f"Среднее количество операций: {avg_insert_ops}\n\n")

    file.write("Поиск\n")
    file.write(f"Среднее время: {avg_search_time}\n")
    file.write(f"Среднее количество операций: {avg_search_ops}\n\n")

    file.write("Удаление\n")
    file.write(f"Среднее время: {avg_delete_time}\n")
    file.write(f"Среднее количество операций: {avg_delete_ops}\n")