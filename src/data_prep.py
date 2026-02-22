from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def load_data(as_frame:bool=False, descr:bool=False) -> tuple:
    '''
    Loads the breast cancer dataset from scikit-learn.
    This function retrieves the breast cancer dataset, which is commonly used for
    binary classification tasks in machine learning. The dataset contains features 
    computed from digitized images of breast mass and a target variable indicating 
    the presence of cancer.
    '''

    data = load_breast_cancer(as_frame=as_frame)
    '''
    Docstring for load_data
        :param as_frame: If True, the data is returned as a pandas DataFrame.
        :type as_frame: bool
        :return: A tuple containing the feature dataset (X) and target variable (y).
        :rtype: tuple
    '''
    if descr == True:
        print(f'Description and general information about the dataset\n: {data.DESCR}')
    '''
    Docstring for data.DESCR
        :return: A detailed description of the dataset, including its features, 
                 target variable, and other relevant information.
        :rtype: str 
    '''

    X = data.data
    y = data.target
    '''
    Docstring for X
        :return: Description of the return value
        :rtype: numpy.ndarray
    '''

    return X, y

def prepare_data(X:tuple, y:tuple, size:float, 
                 random_state:int, stratify:bool) -> tuple:
    '''
    Prepares the data for training and testing by splitting it into training 
    and test sets. This function takes the feature dataset (X) and target 
    variable (y) and splits them into training and test sets based on the 
    specified parameters. The size of the test set, random state for 
    reproducibility, and whether to stratify the split can be controlled 
    through the function's parameters.

        :param X: The feature dataset.
        :type X: tuple
        :param y: The target variable.
        :type y: tuple
        :param size: The proportion of the dataset to include in the test split.
        :type size: float
        :param random_state: Controls the randomness of the split for reproducibility.
        :type random_state: int
        :param stratify: Whether to stratify the split based on the target variable.
        :type stratify: bool
        :return: A tuple containing the training and test sets for features and 
                 target variable.
        :rtype: tuple   
    '''

    if size == 'None':
        size = 0.2
    if random_state == 'None':
        random_state = 42
    if stratify == 'None':
        stratify = True
    
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, 
                         test_size=size,
                         random_state=random_state,
                         stratify=y if stratify else None)
    
    return X_train, X_test, y_train, y_test