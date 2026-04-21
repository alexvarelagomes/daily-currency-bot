import logging

def obter_logger(modulo):

    logger = logging.getLogger(modulo)
    
    # Verifica se o logger já tem handlers configurados para evitar duplicação
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Exibe os logs no terminal
        handler = logging.StreamHandler()
        
        # Define o formato do log com data, nível de log, nome do módulo e mensagem
        formatador = logging.Formatter("%(asctime)s - %(levelname)s - [%(name)s] - %(message)s")
        handler.setFormatter(formatador)
        
        logger.addHandler(handler)
        
    return logger