import random
import string
def generate_password(length):
    all_symbols = string.ascii_letters + string.digits + string.punctuation
    required_values = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
    password_list = [random.choice(char_set) for char_set in required_values]
    total_length = length - len(password_list)
    if length > 4:
        for i in range(total_length):
            password_list.append(random.choice(all_symbols))
    random.shuffle(password_list)
    password = "".join(password_list)
    return password
while True:
    user_input = input("Введите длину желаемого пароля: ")
    try:
        length = int(user_input)
        if length > 1000:
            print("Ошибка! Слишком длинный пароль")
        if length < 4:
            print("Для безопасного пароля требуется не менее 4-х символов")
            continue
    except ValueError:
        print("Ошибка! Введите число.")
        continue
    generated_password = generate_password(length)
    print(generated_password)
