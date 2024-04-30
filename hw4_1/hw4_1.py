"""
    У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
    Наприклад:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
    Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
    Вимоги до завдання:
    Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
    Рекомендації для виконання:
    Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.
    Критерії оцінювання:
    Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.
    Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    Очікуваний результат:
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
"""

def total_salary(path):
    total_salary_sum = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:             # We open the file for reading with an indication of encoding
            for line in file:
                values = line.strip().split(',')                    # We separate the line by commas and get a list of values
                if len(values) >= 2:                                # If the list has at least two elements (surname, salary)
                    salary = int(values[1].strip())                 # We get the developer's salary (it is assumed that this is the second element)
                    total_salary_sum += salary                      # We add the salary to the total amount
                    num_developers += 1                             #We increase the counter of developers
        
        if num_developers > 0:                                      # We calculate the average salary
            average_salary = int(total_salary_sum / num_developers)
        return total_salary_sum, average_salary                     # We return a tuple with the total amount and the average salary
    except FileNotFoundError:
        print("\nFile not found.")                                  #File not found case
    except Exception as e:
        print("\nAn error occurred:", e)                            #The case when another error occurred

total, average = total_salary("hw4_1/salary_file.txt")
print(f"\nЗагальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
