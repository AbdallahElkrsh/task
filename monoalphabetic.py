def monoalphabetic_cipher(text, key_from, key_to):
    text = text.upper()
    result = ""
    for char in text:
        if char in key_from:
            result += key_to[key_from.index(char)]
        else:
            result += char  # الاحتفاظ بالمسافات والعلامات الأخرى دون تغيير
    return result

# إدخال الأبجدية المشفرة والمفتاح من المستخدم
plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = input("Enter the cipher alphabet (26 letters, no duplicates): ").upper()

# التحقق من صحة الإدخال
if len(set(cipher_alphabet)) != 26 or len(cipher_alphabet) != 26:
    print("Invalid cipher alphabet! Make sure it contains 26 unique letters.")
else:
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    text = input("Enter the text: ")

    if mode == "encrypt":
        result = monoalphabetic_cipher(text, plain_alphabet, cipher_alphabet)
    elif mode == "decrypt":
        result = monoalphabetic_cipher(text, cipher_alphabet, plain_alphabet)
    else:
        result = "Invalid mode selected!"

    print(f"\nResult ({mode}ed text): {result}")
