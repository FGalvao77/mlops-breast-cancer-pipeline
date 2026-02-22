# Breast Cancer Classification: End-to-End MLOps Pipeline 🎗️

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange.svg)](https://mlflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Serving-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![UV](https://img.shields.io/badge/Package_Manager-UV-blueviolet.svg)](https://github.com/astral-sh/uv)

---

## 🇧🇷 Português (PT-BR)

### 🎯 Objetivo Principal

Este projeto desenvolve uma solução de **MLOps ponta a ponta** para a classificação de tumores de câncer de mama (Benigno vs. Maligno). O foco principal não é apenas a precisão do modelo, mas a criação de um ecossistema robusto que garanta **reprodutibilidade, rastreabilidade e facilidade de deploy**, seguindo as melhores práticas da engenharia de software e ciência de dados.

### 🚀 Etapas do Projeto

1.  **Engenharia de Dados**: Carregamento e preparação do dataset *Breast Cancer* do Scikit-learn, utilizando divisões estratificadas para manter a proporção das classes.
2.  **Pipeline de Modelagem**: Implementação de um `Pipeline` robusto que combina pré-processamento (`StandardScaler`) e o classificador `RandomForest`, garantindo que não haja vazamento de dados (*data leakage*).
3.  **Rastreamento de Experimentos (MLflow)**: Registro automático de hiperparâmetros, métricas (Acurácia, F1-Score, ROC AUC) e artefatos (Matriz de Confusão, Curva ROC) em cada execução.
4.  **Serviço de Predição (API)**: Desenvolvimento de uma API REST com **FastAPI**, incluindo endpoints de saúde (*health checks*), métricas de monitoramento (Prometheus) e predição em lote.
5.  **Interface de Usuário (Streamlit)**: Criação de um dashboard interativo para que usuários não técnicos possam realizar predições e visualizar metadados do modelo de forma intuitiva.
6.  **Gerenciamento de Dependências**: Utilização do **UV**, um gerenciador de pacotes ultrarrápido escrito em Rust, garantindo ambientes virtuais consistentes.

### 📊 Resultados Alcançados

- **Modelo de Alta Performance**: Alcançamos métricas sólidas (Acurácia > 95%), validadas através de métricas detalhadas.
- **Rastreabilidade Total**: Cada versão do modelo e seus respectivos resultados estão catalogados no MLflow.
- **Pronto para Produção**: API estruturada com tratamento de erros, logs e monitoramento básico.

### 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Ciência de Dados**: Scikit-learn, Pandas, NumPy, Joblib
- **MLOps**: MLflow
- **Deploy/Serviço**: FastAPI, Uvicorn, Streamlit
- **Infraestrutura**: UV (Package Manager), Prometheus (Metrics)

### 📈 Próximas Etapas e Melhorias

- [ ] **Dockerização**: Criar containers para a API e o Dashboard para facilitar o deploy em nuvem.
- [ ] **CI/CD**: Implementar GitHub Actions para automação de testes e deploy.
- [ ] **Otimização**: Integrar o Optuna para busca automática de hiperparâmetros.
- [ ] **Monitoramento Avançado**: Implementar Grafana para visualização das métricas do Prometheus em tempo real.

---

## 🇺🇸 English (EN-US)

### 🎯 Main Objective

This project implements an **end-to-end MLOps pipeline** for breast cancer tumor classification (Benign vs. Malignant). The primary goal is not just model accuracy, but the creation of a robust ecosystem that ensures **reproducibility, traceability, and seamless deployment**, adhering to the highest standards of software engineering and data science.

### 🚀 Project Steps

1.  **Data Engineering**: Loading and preparing the Scikit-learn *Breast Cancer* dataset using stratified splits to maintain class balance.
2.  **Modeling Pipeline**: Implementation of a robust `Pipeline` combining preprocessing (`StandardScaler`) and a `RandomForest` classifier to prevent data leakage.
3.  **Experiment Tracking (MLflow)**: Automated logging of hyperparameters, metrics (Accuracy, F1-Score, ROC AUC), and artifacts (Confusion Matrix, ROC Curve) for every run.
4.  **Model Serving (API)**: Development of a REST API using **FastAPI**, featuring health checks, monitoring metrics (Prometheus), and batch prediction endpoints.
5.  **User Interface (Streamlit)**: Creation of an interactive dashboard for non-technical users to perform predictions and visualize model metadata intuitively.
6.  **Dependency Management**: Leveraging **UV**, an ultra-fast package manager written in Rust, to ensure consistent and reproducible virtual environments.

### 📊 Results Achieved

- **High-Performance Model**: Achieved solid metrics (Accuracy > 95%), validated through detailed reporting.
- **Full Traceability**: Every model version and its respective results are cataloged within MLflow.
- **Production-Ready**: A structured API with comprehensive error handling, logging, and basic monitoring.

### 🛠️ Technologies Used

- **Language**: Python 3.10+
- **Data Science**: Scikit-learn, Pandas, NumPy, Joblib
- **MLOps**: MLflow
- **Deployment/Serving**: FastAPI, Uvicorn, Streamlit
- **Infrastructure**: UV (Package Manager), Prometheus (Metrics)

### 📈 Future Roadmap & Improvements

- [ ] **Dockerization**: Containerize the API and Dashboard for easier cloud deployment.
- [ ] **CI/CD**: Implement GitHub Actions for automated testing and deployment pipelines.
- [ ] **Hyperparameter Tuning**: Integrate Optuna for automated hyperparameter optimization.
- [ ] **Advanced Monitoring**: Set up Grafana to visualize Prometheus metrics in real-time.