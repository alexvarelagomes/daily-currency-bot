import os
import sys
from dotenv import load_dotenv

load_dotenv()

from cotacao import buscar_cotacoes
from notificacao import enviar_telegram
from utils.logger import obter_logger
from utils.database import InicializarBanco, SalvarCotacoesDoDia, ConsultarHistoricoDeExecucao

token_telegram = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
hg_api_key = os.getenv("HG_API_KEY")
database_url = os.getenv("DATABASE_URL")

log = obter_logger(__name__)

if __name__ == "__main__":
    if not hg_api_key or not database_url:
        log.error("Chave de API da HG Brasil ou URL do banco de dados não encontrada. Verificar situação.")
        sys.exit(1)

    # Inicia o banco de dados e cria a tabela, caso ela ainda não exista. 
    # Pode ser chamada várias vezes sem causar erros ou criar tabelas duplicadas.
    InicializarBanco()

    if ConsultarHistoricoDeExecucao():
        log.warning("Cotações do dia já foram salvas no banco de dados.")
        sys.exit(0) # Status 0 indica que a execução foi bem-sucedida, mesmo que as cotações já tenham sido salvas anteriormente.    

    valores_hoje = buscar_cotacoes(hg_api_key)

    if valores_hoje:
        log.info("Extração concluída. Iniciando fase de entrega.")

        # Salvando as cotações do dia no banco de dados
        SalvarCotacoesDoDia(valores_hoje)

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