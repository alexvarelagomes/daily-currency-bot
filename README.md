# Daily Currency Bot

Um pipeline ETL (Extract, Transform, Load) stateful e automatizado construído em Python. 
O sistema extrai dados financeiros de uma API autenticada, aplica lógica de precisão decimal, valida o estado da execução em um banco de dados PostgreSQL para garantir idempotência e notifica o usuário via Telegram.

Este projeto demonstra habilidades em consumo de APIs REST, modelagem de dados em nuvem, arquitetura serverless, isolamento de credenciais e automação CI/CD.

## Arquitetura e Fluxo de Dados

O fluxo de execução foi desenhado para ser resiliente e evitar duplicidade de dados (lixo de banco):
1. **State Validation:** Conexão com banco PostgreSQL (Neon) para verificar se o pipeline já rodou na data atual. Se sim, a execução é abortada silenciosamente (Idempotência).
2. **Extract:** Consumo da API HG Brasil Finance para capturar cotações em tempo real (USD, EUR, GBP, CNY, ARS e BTC).
3. **Transform & Load:** Tratamento do JSON, conversão de tipos, aplicação de precisão decimal (DECIMAL 15,4) e persistência do histórico no banco de dados.
4. **Notify:** Entrega de relatório formatado via Telegram Bot API, incluindo informativos de paridade monetária.
5. **Automation:** Orquestração agendada via GitHub Actions utilizando Repository Secrets para segurança das chaves.

## Tecnologias Utilizadas

* **Python 3.13**
* **PostgreSQL (Neon.tech)** (Banco de dados relacional serverless)
* **psycopg2** (Driver de conexão e execução de queries SQL)
* **Requests** (Comunicação HTTP com tratamento de erros)
* **python-dotenv** (Gestão de variáveis de ambiente)
* **uv** (Gerenciamento ultrarrápido de dependências e ambientes virtuais)
* **Telegram Bot API** (Interface de entrega de dados)
* **GitHub Actions** (Automação CI/CD e execução agendada via Cron)

## Como Acessar ou Reproduzir

Existem duas formas de interagir com este projeto:

### 1. Para Usuários Finais (Consumo de Dados)
O bot publica o relatório financeiro automaticamente todos os dias às 11h (BRT). Para receber as cotações, basta ingressar no canal oficial de transmissão no Telegram:
[@BOT_COTACAO](https://t.me/bot_cotacao)

### 2. Para Desenvolvedores (Testes Locais e Deploy)
Se deseja rodar a sua própria instância deste pipeline:

**Para rodar localmente:**
1. Clone este repositório e instale as dependências: `uv sync`.
2. Crie um arquivo `.env` na raiz espelhando o `.env.example` e insira suas credenciais (Telegram, HG Brasil e a `DATABASE_URL` do Neon).
3. Execute o orquestrador: `uv run main.py`.

**Para automação em Nuvem (CI/CD):**
1. Faça um Fork deste repositório.
2. Crie uma instância gratuita no [Neon.tech](https://neon.tech/) e obtenha a sua Connection String.
3. Acesse **Settings > Secrets and variables > Actions** e cadastre as variáveis de ambiente: `TELEGRAM_BOT_TOKEN`, `CHAT_ID`, `HG_API_KEY` e `DATABASE_URL`.
4. Na aba **Actions**, habilite a execução dos workflows. A nuvem assumirá o agendamento Cron de segunda a sexta.

## Prova de Execução

Abaixo está a demonstração do pipeline em funcionamento, entregando o resumo financeiro diário:

![Demonstração do Bot no Telegram](assets/print_telegram.png)