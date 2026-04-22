# Daily Currency Bot

Um pipeline ETL (Extract, Transform, Load) leve e automatizado construído em Python. 
O sistema extrai dados financeiros de uma API autenticada, aplica lógica de precisão decimal dinâmica e notifica o usuário via Telegram.

Este projeto demonstra habilidades em consumo de APIs REST com autenticação, tratamento de dados, isolamento de credenciais e CI/CD.

## Arquitetura e Fluxo de Dados

O fluxo de execução é direto e modularizado:
1. **Extract:** Consumo da API HG Brasil Finance para capturar cotações em tempo real (USD, EUR, GBP, CNY, ARS e BTC).
2. **Transform:** Tratamento do JSON, conversão de tipos e aplicação de precisão decimal variável.
3. **Load / Notify:** Entrega de relatório formatado via Telegram Bot API, incluindo informativos de paridade monetária.
4. **Automation:** Orquestração agendada via GitHub Actions utilizando Repository Secrets para segurança das chaves.

## Tecnologias Utilizadas

* **Python 3.13**
* **Requests** (Comunicação HTTP com tratamento de erros)
* **python-dotenv** (Isolamento de múltiplas credenciais: Telegram e HG Brasil)
* **uv** (Gerenciamento de dependências e ambiente virtual)
* **Telegram Bot API** (Interface de entrega de dados)
* **GitHub Actions** (Automação CI/CD e execução agendada via Cron)

## Como Acessar ou Reproduzir

Existem duas formas de interagir com este projeto:

### 1. Para Usuários Finais (Consumo de Dados)
O bot publica o relatório financeiro automaticamente todos os dias às 11h. Para receber as cotações, basta ingressar no canal oficial de transmissão:
👉 **[Link para o Canal do Telegram]** *(https://t.me/bot_cotacao)*

### 2. Para Desenvolvedores (Fork e CI/CD)
Se deseja rodar a sua própria instância deste pipeline:
1. Faça um Fork deste repositório.
2. Obtenha um Token de Bot no Telegram (@BotFather) e uma API Key na [HG Brasil](https://hgbrasil.com/).
3. No seu repositório, vá em **Settings > Secrets > Actions** e cadastre as chaves: `TELEGRAM_BOT_TOKEN`, `CHAT_ID` e `HG_API_KEY`.
4. Ative os Workflows na aba **Actions**. A automação assumirá a execução diária.

## Prova de Execução

Abaixo está a demonstração do pipeline em funcionamento, entregando o resumo financeiro diário:

![Demonstração do Bot no Telegram](assets/print_telegram.png)
