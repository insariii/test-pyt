# 1

def mood_diary_program():
    mood_diary = {}
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    for day in days:
        mood = input(f"Введите настроение в день '{day}': ")
        mood_diary[day] = mood

    print("Ваш дневник настроений:")
    for day, mood in mood_diary.items():
        print(f"{day}: {mood}")

    mood_count = {}
    for mood in mood_diary.values():
        mood_count[mood] = mood_count.get(mood, 0) + 1

    most_common = max(mood_count, key=mood_count.get)
    print(f"Чаще всего у вас было настроение: {most_common}")


# 2
recipes = {}

def show_recipes():
    if not recipes:
        print("В книге пока нет рецептов.")
    else:
        for i, (name, ingredients) in enumerate(recipes.items(), start=1):
            print(f"{i}. {name}: {', '.join(ingredients)}")

def add_recipe():
    name = input("Введите название блюда: ")
    ingredients = input("Введите ингредиенты через запятую: ").split(",")
    recipes[name] = [ing.strip() for ing in ingredients]

def search_by_ingredient():
    query = input("Введите ингредиент для поиска: ").lower()
    found = [name for name, ing in recipes.items() if query in [i.lower() for i in ing]]
    if found:
        print( ", ".join(found))
    else:
        print("Ничего не найдено.")


while True:
    choice = input("Выберите действие: ")
    if choice == "1":
        show_recipes()
    elif choice == "2":
        add_recipe()
    elif choice == "3":
        search_by_ingredient()
    elif choice == "4":
        break



# 3

students = {}

def add_student():
    name = input("Введите имя студента: ")
    grades = input("Введите оценки через пробел: ").split()
    students[name] = list(map(float, grades))

def add_grade():
    name = input("Введите имя студента: ")
    if name in students:
        grade = float(input("Введите новую оценку: "))
        students[name].append(grade)


def show_averages():
    if not students:
        print("Журнал пуст.")
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f"{name}: {avg}")

def show_statistics():
    if not students:
        print("Нет данных.")
        return
    averages = {name: sum(g) / len(g) for name, g in students.items()}
    best = max(averages, key=averages.get)
    worst = min(averages, key=averages.get)
    top_students = [n for n, a in averages.items() if a >= 4.5]
    print(f"Лучший студент: {best} ({averages[best]})")
    print(f"Худший студент: {worst} ({averages[worst]})")
    print(f"Количество отличников: {len(top_students)}")


while True:
    choice = input("Выберите действие: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        show_averages()
    elif choice == "4":
        show_statistics()
    elif choice == "5"