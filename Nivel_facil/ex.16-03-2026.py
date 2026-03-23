# # Nível Fácil

# Crie uma função chamada create_packing_list que recebe traveler_name e days_per_location como seus parâmetros.

# Esta função gera uma lista de itens para viagem personalizada para um viajante. A lista inclui itens básicos e itens específicos com base na duração total da viagem.

# Passos:

# Some os valores em days_per_location para obter o número total de dias.
# Inclua uma linha para roupas, mencionando o número total de dias.
# Adicione uma linha para produtos de higiene pessoal.
# Se o total de dias > 7, adicione uma linha para sapatos extras.
# Se o total de dias > 10, adicione uma linha para sabão em pó.
# Concatene todas as linhas em uma única string, prefixada com "Packing list for [traveler_name]:".
# Parâmetros:

# traveler_name (str): O nome do viajante.
# days_per_location (list of int): Dias passados em cada local.
# A função retorna uma string com a lista de itens para viagem completa, formatada com o nome do viajante e sugestões específicas com base na duração da viagem.

# # Resolução

def create_packing_list(traveler_name, days_per_location):
    # Write code here

    total_days = 0
    for i in days_per_location:
        total_days += i

    print(f"Packing list for {traveler_name}:")
    print(f"- Clothes for {total_days} days")
    print("- Toiletries")
    
    if total_days > 7:
        print("- Extra shoes")
    if total_days > 10:
        print("- Laundry soap")

