import json  # Импортируем модуль для работы с JSON файлами.

# Открываем файл dump.json в режиме чтения с кодировкой UTF-8.
file = open('dump.json', 'r', encoding='utf-8')
data = json.load(file)  # Загружаем содержимое JSON файла в переменную `data`.
found = False
# Запрашиваем у пользователя ввод номера квалификации.
numb = input("Введите номер квалификации: ")
# Выводим заголовок для результата поиска.
print("\n=============== Результат поиска ===============")
# Перебираем все элементы в загруженных данных (предположительно список словарей).
for skill in data:
    if skill["model"] == "data.skill" and skill["fields"]["code"] == numb:
            skill_code = skill["fields"]["code"]
            skill_title = skill["fields"]["title"]
            found = True # Устанавливаем флаг `found` в True (результат найден).
    # Проверяем, соответствует ли элемент определённым условиям:
    # 1. Ключ 'model' имеет значение 'data.skill'.
    # 2. Поле 'fields' содержит значение для указанного пользователем ключа `code`.
    for item in data:
        if item["model"] == "data.specialty":
                    if item["fields"]["code"] in numb:
                        prof_code = item["fields"]["code"]
                        prof_title = item["fields"]["title"]
                        prof_type = item["fields"]["c_type"]       
# Если ни одного подходящего результата не найдено, выводим соответствующее сообщение.
if not found:
    print("============== Не найдено ===============")
else:
# Если условия выполнены, выводим код и название квалификации.
    print(f"{prof_code} >> Специальность '{prof_title}', {prof_type}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")
