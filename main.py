from cotacao import buscar_cotacoes
from notificacao import enviar_telegram
import os
from dotenv import load_dotenv
from logger import obter_logger

load_dotenv()

token_telegram = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

log = obter_logger(__name__)

if __name__ == "__main__":
    valores_hoje = buscar_cotacoes()

    if valores_hoje:
        log.info("Extração concluída. Iniciando fase de entrega.")
        
        # Enviando a mensagem para o Telegram
        sucesso = enviar_telegram(valores_hoje, token_telegram, chat_id)
        
        if sucesso:
            log.info("Pipeline executado sem erros. Encerrando operação.")
        else:
            log.error("Pipeline concluído com falhas na entrega.")
    else:
        log.error("Pipeline abortado na origem dos dados.")