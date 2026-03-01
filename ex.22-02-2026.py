# Nível Médio

# Escreva uma função process_deli_orders que receba order_codes, promo_codes e retorne uma tupla contendo o total arrecadado e a lista dos códigos promocionais invertidos.

# Sua delicatessen recebe códigos de pedidos em diferentes bases numéricas (binário com prefixo '0b', 
# hexadecimal com prefixo '0x' ou decimal) representando preços em simoleons, além de strings especiais de códigos promocionais que precisam ser invertidas para o seu programa de fidelidade.
# Lógica:

# Converta cada código de pedido para decimal (remova os prefixos, se presentes)
# Some todos os preços convertidos para obter o total arrecadado
# Inverta cada string de código promocional
# Retorne uma tupla: (total_arrecadado, lista_de_promos_invertidos)
# Parâmetros:

# order_codes (lista): Lista de códigos de preço em bases mistas (strings)
# promo_codes (lista): Lista de strings de códigos promocionais para inverter
# Retorna: Tupla contendo o total arrecadado (int) e a lista dos códigos promocionais invertidos (lista). Formato: (150, ['EDOC', 'LAICEPS'])

# Resolução

def process_deli_orders(ordem_codigos, promo_codigos):
    total_earnings = 0
    
    for codigo in ordem_codigos:
        if codigo.startswith('0b'):
            valor = int(codigo, 2)
        elif codigo.startswith('0x'):
            valor = int(codigo, 16)
        else:
            valor = int(codigo, 10)
        
        total_earnings += valor
    
    reversed_promos = [codigo[::-1] for codigo in promo_codigos]
    
    return (total_earnings, reversed_promos)