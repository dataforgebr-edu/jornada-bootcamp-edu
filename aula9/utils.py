import os
from functools import wraps
from sys import stderr

from loguru import logger

pasta_raiz = os.path.dirname(__file__)

logger.remove()

logger.add(
    sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO"
)

logger.add(
    os.path.join(pasta_raiz, "meu_arquivo_de_logs.log"),
    rotation="5 MB",
    retention="7 days",
    format="{time} {level} {message} {file}",
    level="ERROR",
)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada

    return wrapper
