# Nível Médio

# Escreva uma função sort_roommate_item que receba item_name, condition, item_type e retorne um dicionário com a decisão de manter ou descartar e o motivo.

# A função ajuda você a decidir se deve manter ou descartar os pertences bagunçados do seu colega de quarto com base na condição e no tipo do item.

# Condições:

# Mantenha se a condição for "clean" (limpo)
# Mantenha se o tipo do item for "electronics" (eletrônicos) e a condição não for "broken" (quebrado)
# Mantenha se o tipo do item for "book" (livro) e a condição não for "moldy" (mofado)
# Descarte todo o resto
# Parâmetros:

# item_name (str): Nome do item
# condition (str): Condição atual ("clean", "dirty", "stained", "broken", "moldy")
# item_type (str): Tipo do item ("clothing", "electronics", "book")
# Retorna: Dicionário com decisão e motivo. Formato: {"decision": "keep", "reason": "item is clean"}

# Resolução

def sort_roommate_item(item_name, condition, item_type):
    # Write code here

    if condition == "clean":
        situacao = "keep"
        motivo = "item is clean"

    elif item_type == "electronics" and condition != "broken":
        situacao = "keep"
        motivo = "electronics in working condition"

    elif item_type == "book" and condition != "moldy":
        situacao = "keep"
        motivo = "book is readable"
        
    else:
        situacao = "discard"
        motivo = "item does not meet keep criteria"

    dict_items = {
        "decision": situacao,
        "reason": motivo
    }

    return dict_items