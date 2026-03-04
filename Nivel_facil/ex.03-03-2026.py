# Nível Fácil

# Escreva uma função create_name_tag que recebe first_name, last_name e retorna uma string de crachá formatada.

# A função cria um crachá para convidados de reunião de família com formatação adequada para fácil identificação.

# Parâmetros:

# first_name (str): O primeiro nome do convidado
# last_name (str): O sobrenome do convidado
# Retorna: Uma string de crachá formatada. Formato: Hello, my name is [LAST NAME], [first name]

# Resolução

def create_name_tag(first_name, last_name):
    # Write code here
    formatado_nome = first_name.lower()
    formatado_sobrenome = last_name.upper()
    return f"Hello, my name is {formatado_sobrenome}, {formatado_nome}"