import os

from etl import pipeline_calcular_kpi_de_vendas_consolidado

diretorio = os.path.dirname(__file__)
pasta_argumento: str = os.path.join(diretorio, "data")
formato_de_saida: list = ["csv", "parquet"]

pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento, formato_de_saida)
