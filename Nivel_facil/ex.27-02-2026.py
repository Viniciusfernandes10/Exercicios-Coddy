# Nível Fácil

# Escreva uma função create_adoption_record que recebe cats, dogs, location, contact e retorna uma string de registro formatada do centro de adoção.

# A função combina todos os animais de estimação disponíveis com as informações do abrigo em um único registro para o banco de dados do centro de adoção.

# Parâmetros:

# cats (list): Lista de nomes de gatos disponíveis para adoção
# dogs (list): Lista de nomes de cães disponíveis para adoção
# location (str): Endereço do abrigo
# contact (str): Número de telefone do abrigo
# Retorna: String de registro de adoção formatada. Formato: Pets: [cat1, cat2, dog1, dog2] | Location: [location] | Contact: [contact]

# Resolução

def create_adoption_record(cats, dogs, location, contact):
    # Write code here
    pets = cats + dogs

    return f"Pets: {pets} | Location: {location} | Contact: {contact}"