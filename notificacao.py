import requests
from logger import loggers

log = loggers(__name__)

def enviar_telegram(cotacoes: dict, token: str, chat_id: str) -> bool:
    
    if not cotacoes:
        log.warning("Nenhum dado recebido. Notificação cancelada.")
        return False

    mensagem = "📊 *Resumo Financeiro Diário*\n\n"
    for moeda, valor in cotacoes.items():
        mensagem += f"🔹 *{moeda}:* R$ {valor:.2f}\n"

    # URL base da API do Telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "Markdown"
    }

    try:
        log.info("Disparando mensagem para o Telegram...")
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        log.info("Notificação enviada com sucesso.")
        return True
        
    except requests.exceptions.RequestException as erro:
        log.error(f"Falha na comunicação com o Telegram: {erro}")
        return False