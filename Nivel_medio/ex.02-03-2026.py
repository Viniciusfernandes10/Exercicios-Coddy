# Nível Médio

# Escreva uma função create_walk_summary que receba o nome de um cliente, dois valores numéricos como strings (tarifa por hora e minutos caminhados) 
# e os números do quarteirão de início e fim, e então retorne um dicionário completo com o resumo da caminhada.

# Seu resumo deve incluir três coisas:

# tags: Todas as substrings únicas do nome do cliente (para fins de arquivamento/pesquisa)
# route: A sequência mais curta de movimentos para ir do quarteirão inicial ao quarteirão final, onde você só pode se mover para frente (+1) ou para trás (-1) um quarteirão por vez. 
# Retorne isso como uma string, por exemplo, "→→←→" (use → para frente, ← para trás)
# bill: A cobrança total, calculada multiplicando a string da tarifa pela string dos minutos dígito a dígito (trate "12" × "3" como: 1×3=3, 2×3=6, resultando em "36")
# Para a rota, escolha sempre o caminho mais eficiente. 
# Para a multiplicação das strings, se elas tiverem comprimentos diferentes, alinhe-as pela direita e use 0 para os dígitos faltantes à esquerda.

# resolução

def create_walk_summary(name, rate, minutes, start_block, end_block):
    # Write code here
    tags = set()
    name = name.replace(" ", "")
    
    for i in range(len(name)):
        for j in range(i + 1, len(name) + 1):
            tags.add(name[i:j])


    difference = end_block - start_block
    
    if difference > 0:
        route = "→" * difference
    elif difference < 0:
        route = "←" * abs(difference)
    else:
        route = ""


    max_len = max(len(rate), len(minutes))
    
    rate = rate.zfill(max_len)
    minutes = minutes.zfill(max_len)

    bill = ""
    
    for i in range(max_len):
        bill += str(int(rate[i]) * int(minutes[i]))


    return {
        "tags": tags,
        "route": route,
        "bill": bill
    } 