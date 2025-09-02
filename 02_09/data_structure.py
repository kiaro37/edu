# Список (list), изменяемый

fruits = ["apple", "banana", "cherry"]
fruits.append("melon")
fruits.remove("apple")
print(fruits[0])

# Кортеж (tuple), неизменяемый

point = (10, 20)
print(point[0])

# Множество (set), изменяемое

numbers = {1, 2, 3, 4, 3}
print(numbers)

numbers.add(5)
numbers.remove(2)
print(3 in numbers)     #проверка наличия

# Словарь (dict), изменяемый

user = {"name": "Evgeniy", "role": "QA"}
print(user["name"])

user["age"] = 30          #добавление
del user["role"]          #удаление
print(user.keys())
print(user.values())

# Исключения

try:
    x = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")


# Теперь твои мини-задача:
# 1. Создай список из 3 строк. Добавь новый элемент и выведи его.
# 2. Создай множество с повторяющимися элементами, удали один элемент.
# 3. Создай словарь {"username": "test", "password": "1234"}, измени пароль.
# 4. Попробуй поделить число на 0 и обработай исключение.

users = ["Andrey", "Dasha", "Misha"]
users.append("Olya")
print(users[-1])

things = {"table", "knife", "spoon", "spoon"}
things.discard("table")
print(things)

user_data = {"username": "test", "password": "1234"}
user_data["password"] = "5678"
print(user_data.get("password", "Пароля нет"))

try:
    m = 90 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")