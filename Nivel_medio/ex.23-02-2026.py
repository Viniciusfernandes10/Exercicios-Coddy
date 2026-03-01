# Nível Médio

# Crie um programa que ajude a organizar uma reunião de família com duas tarefas. 
# Primeiro, leia dois números inteiros e encontre o dígito principal do primeiro número elevado à potência do segundo (isso ajuda a estimar grandes quantidades). 
# Em seguida, leia uma mensagem de texto e reorganize-a movendo todas as consoantes para o início, mantendo as vogais, espaços e pontuações depois delas — tudo na ordem original.

# Resolução

# Read the two integers
base = int(input())
exponent = int(input())

# Calculate base^exponent and find the leading digit
result = base ** exponent
leading_digit = int(str(result)[0])
print(leading_digit)

# Read the text message
message = input()

# Define vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Separate consonants and non-consonants (vowels, spaces, punctuation)
consonants = []
non_consonants = []

for char in message:
    if char.isalpha() and char not in vowels:
        # It's a consonant
        consonants.append(char)
    else:
        # It's a vowel, space, or punctuation
        non_consonants.append(char)

# Combine consonants first, then non-consonants
rearranged = ''.join(consonants) + ''.join(non_consonants)
print(rearranged)
