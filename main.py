from cotacao import buscar_cotacoes
from logger import loggers

log = loggers(__name__)

if __name__ == "__main__":
    valores_hoje = buscar_cotacoes()

    if valores_hoje:
        for moeda, valor in valores_hoje.items():
            log.info(f"{moeda}: R$ {valor:.2f}")