# Nível Médio

# Escreva uma função setup_coastal_study que recebe livros, nível_da_lâmpada, materiais e retorna um dicionário com a organização do espaço de estudo.

# A função organiza sua área de estudo costeira invertendo os títulos dos livros para melhor arranjo na estante, ajustando o brilho da lâmpada e preparando os materiais.

# Lógica:

# Inverta o título de cada livro alternadamente, começando pelo segundo livro (índices 1, 3, 5, etc.)
# Aumente o nível da lâmpada em 2, depois diminua em 1 para alcançar o brilho ideal
# Inverta toda a lista de materiais para melhor acessibilidade
# Parâmetros:

# livros (lista): Lista de títulos de livros para organizar
# nível_da_lâmpada (int): Nível inicial de brilho
# materiais (lista): Lista de materiais de estudo
# Retorna: Dicionário com a organização do espaço de estudo. Formato:
# {"books": [...], "lamp_level": int, "materials": [...]}

# Resolução

def setup_coastal_study(books, lamp_level, materials):
    # Write code here 
    for i in range(len(books)):
        if i % 2 == 1:
            books[i] = books[i][::-1]
    
    lamp_level += 2
    lamp_level -= 1
    
    materials = materials[::-1]
    
    return {
        "books": books,
        "lamp_level": lamp_level,
        "materials": materials
    }