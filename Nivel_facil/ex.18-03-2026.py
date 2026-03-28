# # Nível Fácil

# Crie uma função chamada moss_field_notes que recebe color, texture e environment como seus parâmetros.

# A função deve ajudar um estudante de biologia, Alex, a categorizar e documentar espécies de musgo durante sua expedição de campo em uma área selvagem remota. 
# Alex não tem acesso a tecnologia moderna, então ele depende de observações e comparações simples.

# A função deve realizar as seguintes tarefas:

# Concatenar os parâmetros de entrada em uma string de nota de campo no formato: "Color: [color], Texture: [texture], Environment: [environment]".
# Comparar a nota de campo gerada com uma lista predefinida de descrições de musgos conhecidos.
# Retornar uma string que inclua a nota de campo e uma identificação provisória se uma correspondência for encontrada, 
# ou uma mensagem indicando que a espécie é potencialmente nova se nenhuma correspondência for encontrada.
# Use a seguinte lista de descrições de musgos conhecidos para comparação:


# known_mosses = [
#     "Color: Green, Texture: Soft, Environment: Shaded forest floor",
#     "Color: Red, Texture: Rough, Environment: Exposed rocks",
#     "Color: Brown, Texture: Fuzzy, Environment: Tree bark",
#     "Color: Yellow, Texture: Spongy, Environment: Wetlands"
# ]
# Parâmetros:

# color (str): A cor observada do musgo.
# texture (str): A textura observada do musgo.
# environment (str): O ambiente onde o musgo foi encontrado.
# A função retorna uma string contendo a nota de campo e o resultado da comparação.

# # Resolução

def moss_field_notes(color, texture, environment):
    # Write code here 
    
    known_mosses = [
        "Color: Green, Texture: Soft, Environment: Shaded forest floor",
        "Color: Red, Texture: Rough, Environment: Exposed rocks",
        "Color: Brown, Texture: Fuzzy, Environment: Tree bark",
        "Color: Yellow, Texture: Spongy, Environment: Wetlands"
    ]
    
    field_note = f"Color: {color}, Texture: {texture}, Environment: {environment}"
    
    if field_note in known_mosses:
        index = known_mosses.index(field_note) + 1
        result = f"Tentative identification: Known moss species #{index}"
    else:
        result = "No match found. This could be a new species!"
    
    return f"{field_note}\n{result}"


