def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(text, key, alphabet):
    key = generate_key(text, key)
    cipher_text = []
    alphabet_size = len(alphabet)

    for i in range(len(text)):
        if text[i] in alphabet and key[i] in alphabet:
            shift = alphabet.index(key[i])
            new_index = (alphabet.index(text[i]) + shift) % alphabet_size
            cipher_text.append(alphabet[new_index])
        else:
            cipher_text.append(text[i])  # Оставляем неизменным, если символ не в алфавите
    return "".join(cipher_text)

def decrypt_vigenere(cipher_text, key, alphabet):
    key = generate_key(cipher_text, key)
    original_text = []
    alphabet_size = len(alphabet)

    for i in range(len(cipher_text)):
        if cipher_text[i] in alphabet and key[i] in alphabet:
            shift = alphabet.index(key[i])
            new_index = (alphabet.index(cipher_text[i]) - shift) % alphabet_size
            original_text.append(alphabet[new_index])
        else:
            original_text.append(cipher_text[i])  # Оставляем неизменным, если символ не в алфавите
    return "".join(original_text)

# Выбор алфавита
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;:!?/()[]<>@#$%^&*' "

while True:    
    text = input("Введите текст шифра (или 'q' для выхода): ")
    if text.lower() == 'q':
        print("Выход из программы.")
        break

    key = input("Введите ключ: ")

    action = input("Выберите номер действия - зашифровать(1)/расшифровать(2): ").strip().lower()

    # Шифрование или дешифрование в зависимости от выбора пользователя
    if action == "1":
        result = encrypt_vigenere(text, key, alphabet)
        print("\nЗашифрованный текст:", result)
    elif action == "2":
        result = decrypt_vigenere(text, key, alphabet)
        print("\nРасшифрованный текст:", result)
    else:
        print("Неверное действие! Выберите 'расшифровать(1)' или 'зашифровать(2)'.")
        continue

    # Запрос на продолжение или выход
    repeat = input("\nВведите 'q' для выхода или нажмите Enter, чтобы продолжить: ").strip().lower()
    if repeat == 'q':
        print("Выход из программы.")
        break

