'''
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while not nome_valido:
    try:
        nome: str = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario: float = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
'''


# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
'''
lista: list = []
lista.extend(range(1, 11))
for i in lista:
    print(i)
'''
# 2. Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".
'''
lista_pronta: list = ["Python", "Java", "C++", "JavaScript"]
lista_pronta.remove("C++")
print(lista_pronta)
lista_pronta.append("Ruby")
print(lista_pronta)
'''
# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
'''
livros: dict = {
    'titulo':'livro1',
    'autor':'autor1',
    'ano':2015
}
for k, v in livros.items():
    print(k, v)
'''
# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
'''
texto_entrada: str = 'essa é uma string válida para um teste'
texto_split: list = list(texto_entrada.replace(" ", ""))
count_letras: dict = {}
for v in texto_split:
    if v in count_letras:
        count_letras[v] += 1
    else:
        count_letras[v] = 1
print(count_letras)
'''
# 5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.
lista: list = ["maçã", "banana", "cereja"]
dicionario: dict = {
    "maçã": 0.45, 
    "banana": 0.30, 
    "cereja": 0.65
}
soma: int = 0

for i in lista:
    soma += dicionario[i]

print(f"a soma é {soma}")

