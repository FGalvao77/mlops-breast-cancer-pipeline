# Importando as bibliotecas e módulos necessários
import mlflow
import mlflow.sklearn

from utils import load_config

from data_prep import load_data, prepare_data

from pathlib import Path
import shutil

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import (classification_report, 
                             confusion_matrix, 
                             ConfusionMatrixDisplay,
                             roc_curve,
                             auc,
                             RocCurveDisplay,
                             precision_score, 
                             recall_score, 
                             f1_score)

import matplotlib.pyplot as plt
plt.style.use(style='ggplot')

import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning)

# Verificando se MLflow está disponível para uso
USE_MLFLOW = False
try:
    import mlflow
    import mlflow.sklearn 
    USE_MLFLOW = True
except ImportError:
    USE_MLFLOW = False

# Função principal: treinamento, avaliação, visualização e etc
def main():

    # Instanciando as configurações através da função "load_config"
    config = load_config(file_path='configs.yaml')
    print(f'\nCONFIG: \n{config}\n')

    # Carregando os dados com a função "load_data"
    X, y = load_data(as_frame=False)

    # Dividindo os dados em conjuntos de treino e teste, usando a função "prepare_data"
    X_train, X_test, y_train, y_test = prepare_data(X=X, y=y, 
                                                    size=config['test_size'], 
                                                    random_state=config['random_state'], 
                                                    stratify=config['stratify'])
    # Exibir as formas dos conjuntos de treino e teste para verificação
    print(f'SHAPES')
    print(f'X_train: {X_train.shape} | X_test: {X_test.shape} | y_train: {y_train.shape} | y_test: {y_test.shape}\n')

    # Criando o pipeline de pré-processamento e modelagem
    pipe = Pipeline(steps=[
        ('scaler', StandardScaler()), 
        ('rf_model', RandomForestClassifier(**config['model']['params']))
    ])

    # Treinando o modelo e realizando as previsões
    pipe.fit(X=X_train, y=y_train)
    y_pred = pipe.predict(X=X_test)

    # Instanciando um objeto para salvar os parâmetros do modelo
    params_dir = Path(config['paths']['params']).resolve()
    # Limpando o diretório se já existir
    if params_dir.exists():
        shutil.rmtree(params_dir)
    # Criando o diretório para salvar os parâmetros do modelo, se não existir
    params_dir.mkdir(parents=True, exist_ok=True)
    # Salvando os parâmetros do modelo em um arquivo "params.txt"
    with open(params_dir / 'model_params.txt', 'w') as f:
        f.write('=' * 80 + '\n')
        f.write('MODEL PARAMETERS\n')
        f.write('=' * 80 + '\n')
        for key, value in config['model']['params'].items():
            f.write(f'{key}: {value}\n')
        f.write('=' * 80 + '\n')
    print(f'Model parameters saved to: {params_dir / "model_params.txt"}')

    # Calculando as métricas de avaliação
    metrics = {
        'accuracy': pipe.score(X=X_test, y=y_test),
        'precision': precision_score(y_true=y_test, y_pred=y_pred),
        'recall': recall_score(y_true=y_test, y_pred=y_pred),
        'f1-score': f1_score(y_true=y_test, y_pred=y_pred)
    }
    # Exibindo as métricas no console
    print(f'METRICS: {metrics}')

    # Gerando o relatório de classificação detalhado
    classification_rep = classification_report(y_true=y_test, y_pred=y_pred)
    # Exibindo o relatório de classificação no console
    print(f'CLASSIFICATION REPORT:\n{classification_rep}')
    
    # Gerando e salvando matriz de confusão
    cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
    # Exibindo a matriz de confusão no console
    print(f'Confusion Matrix:\n{cm}')
    print('=' * 80)

    # Configurando a visualização da matriz de confusão
    plt.figure(figsize=(8, 8))
    ConfusionMatrixDisplay(confusion_matrix=cm,
                           display_labels=pipe.classes_).plot(cmap='Blues')

    plt.title('Confusion Matrix - Random Forest Model\n', 
              fontdict={
                  'fontsize': 15,
                  'fontweight': 'bold'
          })
    
    plt.xlabel(xlabel='Predicted Label', fontsize=12)
    plt.ylabel(ylabel='True Label', fontsize=12)
    plt.grid(visible=False)
    plt.tight_layout()

    # Configurando o diretório para salvar as visualizações (plots)
    plots_dir = Path(config['paths']['plots']).resolve()
    # Limpando o diretório se já existir
    if plots_dir.exists():
        shutil.rmtree(plots_dir)
    # Criando o diretório para salvar as visualizações (plots)
    plots_dir.mkdir(parents=True, exist_ok=True)
    # Salvando a matriz de confusão em artifacts/plots
    plt.savefig(plots_dir / 'confusion_matrix.png', dpi=300, bbox_inches='tight')
    print(f'Confusion matrix saved to: {plots_dir / "confusion_matrix.png"}')
    plt.close()

    # Obtendo as probabilidades para a classe positiva (assumindo classificação binária)
    y_pred_proba = pipe.predict_proba(X=X_test)[:, 1]

    # Gerando os dados para a curva ROC
    fpr, tpr, thresholds = roc_curve(y_true=y_test, y_score=y_pred_proba)
    roc_auc = auc(fpr, tpr)

    # Configurando o diretório para salvar os dados da curva ROC
    roc_curve_data_dir = Path(config['paths']['roc_curve_data']).resolve()
    # Limpando o diretório se já existir
    if roc_curve_data_dir.exists():
        shutil.rmtree(roc_curve_data_dir)
    # Criando o diretório para salvar os dados da curva ROC
    roc_curve_data_dir.mkdir(parents=True, exist_ok=True)
    with open(roc_curve_data_dir / 'roc_curve_data.txt', 'w') as f:
        f.write('=' * 80 + '\n')
        f.write('\t\t\t\tROC CURVE DATA\n')
        f.write('=' * 80 + '\n\n')
        f.write(f'\nFPR: {fpr}\n')
        f.write(f'\nTPR: {tpr}\n')
        f.write(f'\nThresholds: {thresholds}\n')
        f.write('=' * 80 + '\n')

    # Configurando o diretório para salvar as métricas
    metrics_dir = Path(config['paths']['metrics']).resolve()
    # Limpando o diretório se já existir
    if metrics_dir.exists():
        shutil.rmtree(metrics_dir)
    # Criando o diretório para salvar as métricas, se não existir
    metrics_dir.mkdir(parents=True, exist_ok=True)
    # Salvando as métricas e o relatório de classificação em um arquivo txt
    with open(metrics_dir / 'metrics.txt', 'w') as f:
        f.write('=' * 80 + '\n')
        f.write('\t\t\t\tMODEL METRICS\n')
        f.write('=' * 80 + '\n')
        for key, value in metrics.items():
            f.write(f'{key}: {value}\n')
        f.write(f'roc-auc-score: {roc_auc}')
        f.write('\n' + '=' * 80 + '\n\n')
        f.write('=' * 80)
        f.write('\n\t\t\t\tCLASSIFICATION REPORT\n')
        f.write('=' * 80 + '\n')
        f.write(classification_rep)
        f.write('=' * 80 + '\n')
    # Exibindo o caminho do arquivo de métricas salvo
    print(f'Metrics saved to: {metrics_dir / "metrics.txt"}')
    
    # Gerando e salvando o gráfico da curva ROC
    plt.figure(figsize=(8, 6))
    RocCurveDisplay.from_predictions(y_test, y_pred_proba, 
                                     name='Random Forest').plot()
    plt.title('ROC Curve - Random Forest Model\n', 
              fontdict={'fontsize': 15, 
                        'fontweight': 'bold'})
    plt.xlabel('False Positive Rate', fontsize=12)
    plt.ylabel('True Positive Rate', fontsize=12)
    plt.grid(visible=True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(plots_dir / 'roc_curve.png', dpi=300, bbox_inches='tight')
    print(f'ROC curve saved to: {plots_dir / "roc_curve.png"}')
    plt.close()

if __name__ == '__main__':
    main()