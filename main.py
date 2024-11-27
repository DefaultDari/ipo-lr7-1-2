import json

with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


numb = input("Введите номер квалификации: ")

print("\n=============== Результат поиска ===============")
for item in data:
    if item['model'] == 'data.skill' and item['fields'][numb]:
        print(f"{item['fields']['code']} >> {item['fields']['title']}")
        found = True

if not found:
    print("============== Не найдено ===============")