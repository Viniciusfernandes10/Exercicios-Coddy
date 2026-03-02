# Nível Fácil

# Escreva uma função create_plot_label que receba gardener_name, plot_number e retorne uma etiqueta formatada para o canteiro de jardim.

# A função cria uma etiqueta personalizada para cada canteiro, extraindo o primeiro nome e a inicial do sobrenome a partir do nome completo do jardineiro.

# Parâmetros:

# gardener_name (str): Nome completo do jardineiro (primeiro e último nome separados por espaço)
# plot_number (int): Número do canteiro atribuído ao jardineiro
# Retorna: String da etiqueta do canteiro formatada. Formato: Plot [número]: [primeiro nome] [inicial do sobrenome].


# Resolução

def create_plot_label(gardener_name, plot_number):
    # Write code here
    partes = gardener_name.split()
    
    primeiro_nome = partes[0]
    sobrenome = partes[1]
    
    inicial = sobrenome[0]
    
    etiqueta = f"Plot {plot_number}: {primeiro_nome} {inicial}."
    
    return etiqueta