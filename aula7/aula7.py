from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

def contar_valores_unicos(lista: List[float]) -> int:
    return len(set(lista))

def celsius_para_fahrenheit(temperatura_celsius: List[float]) -> List[float]:
    return [(9/5 * temp) + 32 for temp in temperatura_celsius]

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 5

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - sequencia)