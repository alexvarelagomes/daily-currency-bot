from cotacao import CotacaoMoedaConverter

# Bloco para testar se o nosso script está funcionando
if __name__ == "__main__":
    conversor = CotacaoMoedaConverter()
    valores_hoje = conversor.buscar_cotacoes()

    if valores_hoje:
        for moeda, valor in valores_hoje.items():
            # Formatando para mostrar 2 casas decimais, padrão de dinheiro
            print(f"{moeda}: R$ {valor:.2f}")