import requests

class CotacaoMoedaConverter:
    def __init__(self):
        pass

    def buscar_cotacoes(self):
        """
        Consome a AwesomeAPI para buscar cotações de moedas e cripto.
        Retorna um dicionário com os valores de compra (bid).
        """
        # A URL já pede especificamente Dólar, Euro e Bitcoin contra o Real
        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

        # Fazendo a requisição GET para a API
        response = requests.get(url)
        
        # O raise_for_status() é uma boa prática! Ele gera um erro se a API estiver fora do ar
        response.raise_for_status()  
        
        # Convertendo a resposta da API (que vem em JSON) para um dicionário Python
        dados = response.json()
        
        # Extraindo apenas o valor atual (bid) e formatando
        # Convertendo a string que a API devolve para float (número decimal)
        cotacoes = {
            "Dólar": float(dados["USDBRL"]["bid"]),
            "Euro": float(dados["EURBRL"]["bid"]),
            "Bitcoin": float(dados["BTCBRL"]["bid"])
        }
        
        return cotacoes