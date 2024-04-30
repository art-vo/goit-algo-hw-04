'''
    У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
    Наприклад:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
    Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.
    Вимоги до завдання:
    Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.
    Рекомендації для виконання:
    Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.
    Критерії оцінювання:
    Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.
    Приклад використання функції:
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
    Очікуваний результат:
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
'''

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:     # We open the file for reading with an indication of encoding
            for line in file:
                values = line.strip().split(',')            # We separate the line by commas and get a list of values
                if len(values) >= 3:                        # If the list has at least three elements (id, name, age)
                    cat_info = {                            # We create a dictionary with information about the cat and add it to the list
                        "id": values[0].strip(),
                        "name": values[1].strip(),
                        "age": values[2].strip() }
                    cats_info.append(cat_info)
        return cats_info                                    # We return the list of dictionaries with information about cats

    except FileNotFoundError:
        print("File not found.")                            # File not found case
    except Exception as e:
        print("An error occurred:", e)                      # The case when another error occurred

cats_info = get_cats_info("hw4_2/cats_file.txt")
print(cats_info)
