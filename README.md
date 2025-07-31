# Predição de Inadimplência - Brazilian Real Bank Dataset

Este projeto tem como objetivo a construção de um pipeline completo de **machine learning para previsão de inadimplência bancária**, utilizando uma base de dados realista do setor financeiro brasileiro.

> Projeto voltado para **processos seletivos em bancos, fintechs e empresas de crédito**, com foco em boas práticas de engenharia de dados, modelagem preditiva e MLOps.

---

## Objetivo

Prever a **probabilidade de inadimplência** de um cliente com base em dados históricos e demográficos, de forma que o modelo possa ser utilizado como suporte à decisão para concessão de crédito.

O modelo retorna uma **probabilidade (score)** e uma **decisão binária** (inadimplente / não inadimplente).

---

## Tecnologias e Ferramentas

| Categoria | Ferramenta |
|----------|------------|
| Gerenciador de projeto | [Kedro](https://github.com/kedro-org/kedro) |
| Pipelines orquestradas | [Apache Airflow](https://airflow.apache.org/) |
| Modelagem | XGBoost, Redes Neurais (PyTorch/Sklearn) |
| Balanceamento de classes | SMOTE |
| Explainability | SHAP |
| Armazenamento de experimentos | MLflow |
| API para deploy | FastAPI |
| Containerização | Docker |
| Deploy na nuvem | AWS (SageMaker ou ECS) |
| Monitoramento | MLflow + evidência de drift |
| CI/CD | GitHub Actions |
| Testes | Pytest |

---

## Sobre os Dados

O projeto utiliza o **Brazilian Real Bank Dataset**, disponibilizado no [Kaggle](https://www.kaggle.com/datasets/sufyant/brazilian-real-bank-dataset). A base contém dados anonimizados de um banco brasileiro, incluindo:

- Informações demográficas dos clientes
- Comportamento financeiro
- Histórico de pagamento e crédito
- Rótulo de inadimplência

> **Uso exclusivo educacional.** Esta base não representa dados oficiais ou operacionais de instituições financeiras.

---

## Pipeline

O projeto é estruturado em múltiplas etapas com Kedro + Airflow:

1. **Aquisição e ingestão dos dados**
2. **Anonimização e limpeza**
3. **Exploração dos dados (EDA)**
4. **Engenharia de features**
5. **Tratamento de desbalanceamento com SMOTE**
6. **Treinamento de modelos (XGBoost e MLP)**
7. **Avaliação com AUC-ROC, F1-score e KS-statistic**
8. **Explainability (SHAP)**
9. **Empacotamento com Docker**
10. **Serviço REST com FastAPI**
11. **Deploy na AWS**
12. **Monitoramento com MLflow**
13. **Orquestração com Airflow**
14. **CI/CD com GitHub Actions**
15. **Gatilho de re-treino via data drift**

---

## Métricas de Avaliação

Serão utilizadas as seguintes métricas para avaliar performance:

- `AUC-ROC`: capacidade de separação
- `F1-score`: equilíbrio entre precisão e recall
- `KS-statistic`: discriminatividade em crédito
- `Precision@k`: para priorização de concessão

---

## Diferenciais Técnicos

- Estrutura de projeto escalável com Kedro
- Deploy completo com REST API (FastAPI) + Docker + AWS
- CI/CD com GitHub Actions
- Detecção de drift e gatilho de re-treino
- Explicabilidade com SHAP para uso em contextos regulatórios (LGPD, fairness)
- Modularidade para uso com dados reais em produção

---

## Fairness & Conformidade

O modelo será auditado quanto a possíveis **viéses em variáveis sensíveis** (ex: gênero, raça, renda), com foco em conformidade com a LGPD e transparência algorítmica.

---

## Autor

Este projeto foi desenvolvido por Gabriel Zaniboni como parte de um portfólio profissional para aplicações em **Data Science em bancos e fintechs**.

[LinkedIn](https://www.linkedin.com/in/gabrielfz/) • [GitHub](https://github.com/zai-ds)

---
## Disclaimer
Este projeto é educacional e não representa decisões reais de crédito. Todos os dados foram anonimizados. As decisões de concessão de crédito devem envolver critérios éticos, legais e humanos.

## Organização do Projeto

```bash
credit-default-ml/
├── data/
├── notebooks/
├── src/
│   └── credit_scoring/
│       ├── pipelines/
│       │   ├── data_ingestion/
│       │   ├── data_processing/
│       │   ├── feature_engineering/
│       │   └── modeling/
├── tests/
├── docker/
├── .github/workflows/
├── README.md
└── pyproject.toml
