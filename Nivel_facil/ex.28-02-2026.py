# Nível Fácil

# Escreva uma função check_camping_essentials que recebe dois arrays: gear (equipamentos de camping) e snacks (mantimentos), e retorna uma lista combinada de itens para empacotar junto com a informação se todos os itens essenciais estão presentes.

# A função concatena ambos os arrays em uma lista mestre de itens para empacotar, e então verifica se os itens essenciais "tenda" e "saco de dormir" estão incluídos.

# Parâmetros:

# gear (lista): Array de itens de equipamento de camping
# snacks (lista): Array de itens de comida e lanches
# Retorna: Um dicionário com duas chaves: "packing_list" contendo o array combinado de todos os itens, e "has_essentials" como um booleano indicando se tanto "tenda" quanto "saco de dormir" estão presentes. Formato:
# {"packing_list": ["item1", "item2", ...], "has_essentials": true/false}

# Resolução

def check_camping_essentials(gear, snacks):
    # Write code here 
    
    packing_list = list(gear + snacks)

    has_essentials = "tent" in packing_list and "sleeping bag" in packing_list
        
    
    dict_camping = {
        "packing_list": packing_list,
        "has_essentials": has_essentials
    }

    return dict_camping