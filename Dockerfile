FROM python:3.13-slim AS builder

WORKDIR /app

# Copia o arquivo pyproject.toml e o arquivo de lock.
COPY pyproject.toml .
COPY uv.lock .

# Instala as dependências do pyproject.toml usando o uv
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir uvicorn \
    && pip install --no-cache-dir -r <(uvicorn install)

FROM python:3.13-slim

WORKDIR /app

# Copia as dependências instaladas no estágio de build
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copia os arquivos da aplicação
COPY . .

# Expõe a porta que a aplicação irá rodar.
EXPOSE 8000

# Comando para rodar a aplicação com uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]