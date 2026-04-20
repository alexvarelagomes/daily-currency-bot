import requests
import time
from logger import obter_logger

log = obter_logger(__name__)

def buscar_cotacoes(tentativas=3, atraso=60) -> dict:

    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    for tentativa in range(1, tentativas + 1):
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
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Limite de requisições atingido
                log.warning(f"Tentativa {tentativa} de {tentativas}. Aguardando {atraso} segundos antes de tentar novamente.")
                time.sleep(atraso)
            else:
                log.error(f"Erro HTTP: {e}")
                return None
        
        except requests.exceptions.RequestException as e:
            log.error(f"Falha na comunicação com a AwesomeAPI: {e}")
            return None
        
    log.error("Todas as tentativas de extração falharam.")
    return None