import csv


def ler_csv(file: str) -> list:
    try:
        with open(file,  mode="r", newline='') as file:
            csv_read = csv.DictReader(file, delimiter=";")
            return list(csv_read)
    except Exception as e:
        print(f"Erro no import do arquivo: \n menssagem: {e}")
        return None

def processas_dados(dados: list) -> dict:
    try:
        dict_processado = {}
        '''
        # Como fazer sem usar o setDefault
        if row["categoria"] in dict_processado:
            dict_processado[row["categoria"]].append(row)
            print(dict_processado)
        else:
            dict_processado[row["categoria"]] = [row]
            print(dict_processado)
        '''
        for row in arquivo_csv:
            dict_processado.setdefault(row["categoria"], []).append(row)
        return dict_processado
    except Exception as e:
        print(f"Erro no processamento do arquivo: \n menssagem: {e}")
        return None

def calcular_vendas_categoria(vendas: dict) -> dict:
    try:            
        vendas_categoria = {}

        for key, value in dados_tratados.items():
            # print(key, value)
            for item in value:
                if item["categoria"] in vendas_categoria:
                    vendas_categoria[item["categoria"]] += float(item["preco"]) * int(item["quantidade"])
                else: 
                    vendas_categoria[item["categoria"]] = float(item["preco"]) * int(item["quantidade"])
        return vendas_categoria
    except Exception as e:
        print(f"Erro no cálculo das vendas: \n menssagem: {e}")
        return None
    

arquivo_csv = ler_csv("aula7/data/vendas.csv")
# [print(f"{r}\n") for r in arquivo_csv]

dados_tratados = processas_dados(arquivo_csv)
# print(dados_tratados)

vendas = calcular_vendas_categoria(dados_tratados)
print(vendas)
