import glob
import os

import pandas as pd
from decorator_time import time_measure_decorator
from utils import log_decorator

# uma funcao de extract que le e consolida os json


@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# uma funcao que transforma


@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    # return df
    raise ValueError("Erro intencional")


@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list, pasta_saida: str):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in format_saida:
        if formato == "csv":
            df.to_csv(os.path.join(pasta_saida, "dados.csv"), index=False)
        if formato == "parquet":
            df.to_parquet(os.path.join(pasta_saida, "dados.parquet"), index=False)


@log_decorator
@time_measure_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida, pasta)


# pipeline_calcular_kpi_de_vendas_consolidado()
# uma funcao que da load em csv ou parquet
