import requests
from logger import loggers

log = loggers(__name__)

def buscar_cotacoes():

    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        
        dados = response.json()
        
        # Convertendo a string que a API devolve para número decimal
        cotacoes = {
            "Dólar": float(dados["USDBRL"]["bid"]),
            "Euro": float(dados["EURBRL"]["bid"]),
            "Bitcoin": float(dados["BTCBRL"]["bid"])
        }
        
        return cotacoes
    
    except requests.exceptions.RequestException as e:
        log.error(f"Falha na comunicação com a AwesomeAPI: {e}")
        return None