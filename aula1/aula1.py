CONSTANCE_BONUS_FIXO = 1000

nome_usuario = input("Digite o seu nome: ")
valor_salario = float(input("Digite o valor do seu salário: "))
fator_bonus = float(input("Digite o fator de bônus: "))

total_bonus = CONSTANCE_BONUS_FIXO + (valor_salario * fator_bonus)

print(f"Olá, {nome_usuario} seu salaário total foi de {total_bonus}")