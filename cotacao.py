import requests
from utils.logger import obter_logger

log = obter_logger(__name__)

def buscar_cotacoes(api_key: str):

    url = f"https://api.hgbrasil.com/finance?key={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        
        dados = response.json()

        if dados.get("valid_key") is False:
            log.error("Chave de API da HG Brasil rejeitada.")
            return None
        
        # Navegar no formato específico da resposta para extrair as cotações(JSON).
        moedas = dados.get("results", {}).get("currencies", {})
        
        # Convertendo a string que a API devolve para número decimal
        cotacoes = {
            "Dolar": float(moedas["USD"]["buy"]),
            "Euro": float(moedas["EUR"]["buy"]),
            "Libra": float(moedas["GBP"]["buy"]),
            "Renminbi Chinês": float(moedas["CNY"]["buy"]),
            "Peso Argentino": float(moedas["ARS"]["buy"]),
            "Bitcoin": float(moedas["BTC"]["buy"])
        }
        
        return cotacoes
    
    except requests.exceptions.RequestException as e:
        log.error(f"Falha na comunicação com a API: {e}")
        return None
    
    except KeyError as e:
        log.error(f"Formato inesperado na resposta da API: {e}")
        return None