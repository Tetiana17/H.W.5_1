import string
import keyword

user = input("введи рядок:")

result = True

# перевірка не починається з цифр
if user[0].isdigit():
    result = False

# лише великі літери
elif any(char.isupper() for char in user):
    result = False

elif any(char in string.punctuation.replace('_', "") for char in user):
    result = False

# перевірка на наявність пробілів
elif " " in user:
    result = False

# перевірка на ключові слова
elif user in keyword.kwlist:
    result = False

# перевірка на кількість нижніх підкреслень
elif user.count("__") > 0:
    result = False

print(result)
