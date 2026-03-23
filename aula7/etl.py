import csv


def ler_csv(file: str) -> list[dict]:
    try:
        with open(file, mode="r", newline="") as file:
            csv_read = csv.DictReader(file, delimiter=";")
            return list(csv_read)
    except Exception as e:
        print(f"Erro no import do arquivo: \n menssagem: {e}")
        return None


def processas_dados(dados: list) -> dict:
    try:
        dict_processado = {}
        """
        # Como fazer sem usar o setDefault
        if row["categoria"] in dict_processado:
            dict_processado[row["categoria"]].append(row)
            print(dict_processado)
        else:
            dict_processado[row["categoria"]] = [row]
            print(dict_processado)
        """
        for row in dados:
            dict_processado.setdefault(row["categoria"], []).append(row)
        return dict_processado
    except Exception as e:
        print(f"Erro no processamento do arquivo: \n menssagem: {e}")
        return None


def calcular_vendas_categoria(vendas: dict) -> dict:
    """
    Função para calcular os valores das vendas e retornar um dicionário
    """
    try:
        vendas_categoria = {}

        for key, value in vendas.items():
            # print(key, value)
            for item in value:
                vendas_categoria[key] = vendas_categoria.get(key, 0) + float(
                    item["preco"]
                ) * int(item["quantidade"])
                # if item["categoria"] in vendas_categoria:
                #     vendas_categoria[item["categoria"]] += float(item["preco"]) * int(item["quantidade"])
                # else:
                #     vendas_categoria[item["categoria"]] = float(item["preco"]) * int(item["quantidade"])
        return vendas_categoria
    except Exception as e:
        print(f"Erro no cálculo das vendas: \n menssagem: {e}")
        return None
