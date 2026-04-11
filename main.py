from cotacao import CotacaoMoedaConverter

if __name__ == "__main__":
    conversor = CotacaoMoedaConverter()
    valores_hoje = conversor.buscar_cotacoes()

    if valores_hoje:
        for moeda, valor in valores_hoje.items():
            print(f"{moeda}: R$ {valor:.2f}")