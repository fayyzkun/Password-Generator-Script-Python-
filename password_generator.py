import random
import string
n = int(input("введите количество чисел, для создания пароля:"))
def generate_password(n):
    chars = string.ascii_letters + string.digits
    password = ""

    while len(password) < n:
        password += random.choice(chars)
    return password

password = generate_password(n)

with open("password.txt", "a") as f:
    f.write(password + "\n")

print("Пароль сохранен:", password)

