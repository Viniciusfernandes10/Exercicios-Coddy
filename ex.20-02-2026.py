# Desafio fácil

# Crie um programa que valide as informações dos clientes para o programa de fidelidade da sua sanduicheria. 
# Leia um nome de usuário, um saldo de conta e a posição do cliente na fila.
# Verifique se o nome de usuário é válido (3 a 15 caracteres, apenas letras/números/sublinhados, não pode começar com número), 
# confirme se o saldo é um número decimal válido e calcule o tempo estimado de espera (5 minutos por cliente à frente na fila). 
# Imprima "Válido" ou "Inválido" para cada verificação, seguido do tempo de espera em minutos.

# Resolução

# Read the customer information
username = input()
balance = input()
queue_position = int(input())

# TODO: Validate the username
# Check if length is between 3-15 characters
# Check if it contains only letters, numbers, and underscores
# Check if it doesn't start with a number

username_valid = False  # Replace with your validation logic

if 3 <= len(username) <= 15:
    username_valid = True

    # Check if starts with number
    if '0' <= username[0] <= '9':
        username_valid = False

    # Check allowed characters
    for char in username:
        if not (char.isalnum() or char == "_"):
            username_valid = False
            break

# TODO: Validate the balance
# Check if the balance string represents a valid decimal number

balance_valid = False  # Replace with your validation logic

try:
    float(balance)
    balance_valid = True
except:
    balance_valid = False

# TODO: Calculate estimated wait time
# Each customer ahead takes 5 minutes

wait_time = queue_position * 5

# Print the results
if username_valid:
    print("Valid")
else:
    print("Invalid")

if balance_valid:
    print("Valid")
else:
    print("Invalid")

print(wait_time)
