nome_usuario = input("Digite o seu nome: ")
valor_salario = input("Digite o valor do seu salário: ")
fator_bonus = input("Digite o fator de bônus: ")

print(f"{nome_usuario} seu salaário total foi de {1000 + (int(valor_salario) * float(fator_bonus))}")