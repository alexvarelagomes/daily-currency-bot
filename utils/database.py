import os
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.logger import obter_logger

log = obter_logger(__name__)


def ObterConexaoBDNeon():

    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        log.error("URL do banco de dados não foi encontrada no ambiente.")
        raise ValueError("A string de conexão com o banco não está configurada.")

    # Cria uma conexão com o banco de dados PostgreSQL na nuvem.
    return psycopg2.connect(db_url)


def InicializarBanco():

    with ObterConexaoBDNeon() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS cotacoes_historico (
                id SERIAL PRIMARY KEY,
                nome_moeda TEXT NOT NULL,
                valor_compra DECIMAL(15, 4) NOT NULL,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP )""")
            
            conexao.commit() # Salva as alterações no banco de dados


def ConsultarHistoricoDeExecucao():
    
    with ObterConexaoBDNeon() as conexao:
        with conexao.cursor() as cursor:

    # Consulta para verificar se há registros de cotações do dia atual no banco de dados.
    # A função DATE('now') é usada para comparar apenas a data, ignorando a hora, garantindo que seja considerado apenas o dia atual.
            cursor.execute("""
                SELECT 1 FROM cotacoes_historico
                WHERE data_hora::date = CURRENT_DATE
                LIMIT 1 """)
    
            resultados = cursor.fetchone() # fetchone() mostra apenas um resultado, ou None se não houver registros correspondentes.
            return resultados is not None # Retorna True se houver registros do dia atual, ou False caso contrário.


def SalvarCotacoesDoDia(cotacoes: dict): # Salva as cotações do dia no banco de dados, recebendo um dicionário com os nomes das moedas e seus respectivos valores.
    
    if not cotacoes: # Verifica se o dicionário de cotações está vazio
        log.warning("Nenhuma cotação para salvar no banco de dados.")
        return False

    with ObterConexaoBDNeon() as conexao:
        with conexao.cursor() as cursor:
            #Loop para inserir cada cotação no banco de dados.
            for moeda, valor in cotacoes.items(): 
                cursor.execute("""
                    INSERT INTO cotacoes_historico (nome_moeda, valor_compra)
                    VALUES (%s, %s) """, (moeda, valor))
                
        conexao.commit()

    log.info("Cotações salvas com sucesso no histórico do banco de dados.")
    return True


