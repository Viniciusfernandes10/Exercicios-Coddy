# Nível Fácil

# Crie uma função chamada prepare_pet_welcome que recebe pet_name, pet_type e initial_supplies como seus parâmetros.

# A função deve ajudar uma família a preparar uma mensagem de boas-vindas e uma lista de suprimentos para seu novo animal de estimação.

# Sua tarefa é criar uma mensagem de boas-vindas personalizada usando o nome e o tipo do animal de estimação, e então adicionar três itens essenciais à lista de suprimentos com base no tipo do animal.

# Parâmetros:

# pet_name (str): O nome do novo animal de estimação.
# pet_type (str): O tipo de animal de estimação (por exemplo, "dog", "cat", "hamster").
# initial_supplies (list): Uma lista de suprimentos que a família já possui.
# A função deve realizar as seguintes operações:

# Crie uma mensagem de boas-vindas usando concatenação de strings no formato: "Welcome home, [pet_name] the [pet_type]!"
# Adicione três itens essenciais à lista de suprimentos com base no tipo de animal de estimação:
# Para um cachorro: adicione "leash", "dog food" e "chew toy"
# Para um gato: adicione "litter box", "cat food" e "scratching post"
# Para qualquer outro tipo de animal de estimação: adicione "cage", "food" e "toys"
# A função retorna um dicionário com duas chaves: "welcome_message" (string) contendo a mensagem de boas-vindas personalizada, e "supplies" (list) contendo a lista atualizada de suprimentos.

# Resolução

def prepare_pet_welcome(pet_name, pet_type, initial_supplies):
    # Write code here 
    menssagem = "Welcome home, " + pet_name + " the " + pet_type + "!"
    pet_type = pet_type.lower()

    if pet_type == "dog":
        initial_supplies.extend(["leash", "dog food", "chew toy"])
    elif pet_type == "cat":
        initial_supplies.extend(["litter box", "cat food", "scratching post"])
    else:
        initial_supplies.extend(["cage", "food", "toys"])

    dict_animal = {
        "welcome_message": menssagem,
        "supplies": initial_supplies
    }

    return dict_animal
