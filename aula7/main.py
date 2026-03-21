from etl import ler_csv, processas_dados, calcular_vendas_categoria

def main():
    arquivo_csv = ler_csv("aula7/data/vendas.csv")
    # [print(f"{r}\n") for r in arquivo_csv]

    dados_tratados = processas_dados(arquivo_csv)
    # print(dados_tratados)

    vendas = calcular_vendas_categoria(dados_tratados)
    [print(f"Categoria: {k}, valor: {v}") for k, v in vendas.items()]

if __name__ == '__main__':
    main()
