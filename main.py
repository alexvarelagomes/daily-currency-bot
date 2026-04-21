from cotacao import buscar_cotacoes
from notificacao import enviar_telegram
import os
import sys
from dotenv import load_dotenv
from logger import obter_logger

load_dotenv()

token_telegram = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
hg_api_key = os.getenv("HG_API_KEY")

log = obter_logger(__name__)

if __name__ == "__main__":
    valores_hoje = buscar_cotacoes(hg_api_key)

    if valores_hoje:
        log.info("Extração concluída. Iniciando fase de entrega.")
        
        # Enviando a mensagem para o Telegram
        sucesso = enviar_telegram(valores_hoje, token_telegram, chat_id)
        
        if sucesso:
            log.info("Pipeline executado sem erros. Encerrando operação.")
        else:
            log.error("Pipeline concluído com falhas na entrega.")
            sys.exit(1)
    else:
        log.error("Pipeline abortado na origem dos dados.")
        sys.exit(1)