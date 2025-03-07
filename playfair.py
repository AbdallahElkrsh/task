def generate_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set()

    for char in keyword.upper():
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_cipher(text, matrix, mode="encrypt"):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'

    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # نفس الصف
            if mode == "encrypt":
                result += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
            else:
                result += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]

        elif col_a == col_b:  # نفس العمود
            if mode == "encrypt":
                result += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
            else:
                result += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]

        else:  # مربع
            result += matrix[row_a][col_b] + matrix[row_b][col_a]

    return result

# أخذ الإدخال من المستخدم
keyword = input("Enter the keyword for Playfair Cipher: ").upper()
matrix = generate_playfair_matrix(keyword)

print("\nGenerated Playfair Matrix:")
for row in matrix:
    print(row)

text = input("\nEnter the text to encrypt/decrypt: ").upper()
mode = input("Choose mode (encrypt/decrypt): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode selected!")
else:
    result = playfair_cipher(text, matrix, mode)
    print(f"\nResult ({mode}ed text): {result}")
