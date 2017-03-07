from sklearn.datasets import load_iris                  # we'd like to use off-the-shelf data for demonstration
from sklearn.model_selection import train_test_split    # we need to split train and test partitions
import numpy as np                                      # we'd like to calculate things with vectors
import pandas as pd                                     # we may need to use Pandas dataframe

iris_raw = load_iris() # load the off-the-shelf iris data

# store the Iris information onto Pandas DataFrame
iris_data = pd.DataFrame(data = iris_raw['data'], columns = ['sepal_length'] + ['sepal_width'] + ['petal_length'] + ['petal_width']) 
iris_class = pd.DataFrame(data = iris_raw['target'], columns = ['classes']) 
# split the data into training and testing partitions
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_class, test_size=0.2, random_state=0)

'''
sigmoid function: 
    given a vlaue (can be np vector) x, return (1 / 1+np.exp(x))
'''
def sigmoid(x):
    return(1 / 1 + np.exp(x))


