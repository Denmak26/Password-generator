import random
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

num = int(input('Скільки паролей вам потрібно? '))

length = int(input('Якої довжини має бути пароль? '))

if input('Чи потрібні цифри в паролі? (y - якщо так, n - якщо ні) ' ) == 'y':
    chars += DIGITS
else:
    chars = chars
if input('Чи потрібні маленькі букви в паролі? (y - якщо так, n - якщо ні) ' ) == 'y':
    chars += LOWERCASE_LETTERS
else:
    chars = chars
if input('Чи потрібні великі букви в паролі? (y - якщо так, n - якщо ні) ' ) == 'y':
    chars += UPPERCASE_LETTERS
else:
    chars = chars
if input('Чи потрібні знаки пунктуації в паролі? (y - якщо так, n - якщо ні) ' ) == 'y':
    chars += PUNCTUATION
else:
    chars = chars

def generate_password(n,chars):
    passwords = []
    for i in range(num):
        s = []
        for j in range(n):
            s.extend(random.choice(chars))
        passwords.append(''.join(s))
    return passwords

print("Ваші паролі:",*generate_password(length,chars))