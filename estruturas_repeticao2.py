# Microatividade 4: for

# 1. Iterando sobre caracteres de uma string
texto = 'Olá, laço for.'
for item in texto:
    print(f'Caractere: {item}')

print("-" * 20)

# 2. Iterando sobre um intervalo numérico (1 a 10)
# range(1, 11) porque o final é exclusivo
for numero in range(1, 11):
    print(f'Número do intervalo: {numero}')