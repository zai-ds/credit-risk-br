# Imagem base com Python
FROM python:3.10-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto
COPY src/ ./src/
COPY data/06_models/model.pkl ./data/06_models/model.pkl

# Instala dependências
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn pandas xgboost

# Expõe a porta padrão do Uvicorn
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "credit_risk_br.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
