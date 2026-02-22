from platform import platform, python_version
import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib 

# [POR-BR] Teste simples para verificar o ambiente de execução
# [ENG] Simple test to check the execution environment
def test_environment():
    '''
    [POR-BR] Testa o ambiente de execução imprimindo informações sobre 
    a plataforma e a versão do Python.

    [ENG] Tests the execution environment by printing information about
    the platform and Python version.
    '''

    print('\n\tTesting environment...')
    print('=' * 80)
    print(f'Platform: {platform()}')
    print(f'Python version: {python_version()}')
    print(f'Pandas version: {pd.__version__}')
    print(f'Numpy version: {np.__version__}')
    print(f'Scikit-learn version: {sk.__version__}')
    print(f'Matplotlib version: {matplotlib.__version__}')
    print('=' * 80)
    print('Environment test completed successfully.\n')

# [POR-BR] Executar o teste de ambiente quando este script for executado diretamente
# [ENG] Run the environment test when this script is executed directly
if __name__ == '__main__':
    test_environment()