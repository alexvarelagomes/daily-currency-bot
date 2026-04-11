import requests

class CotacaoMoedaConverter:
    def __init__(self):
        pass

    def buscar_cotacoes(self):

        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

        response = requests.get(url)
        
        if response.status_code != 200:
            raise ValueError("Erro ao buscar cotações")
        
        # Dicionário em Python
        dados = response.json()
        
        # Convertendo a string que a API devolve para número decimal
        cotacoes = {
            "Dólar": float(dados["USDBRL"]["bid"]),
            "Euro": float(dados["EURBRL"]["bid"]),
            "Bitcoin": float(dados["BTCBRL"]["bid"])
        }
        
        return cotacoes