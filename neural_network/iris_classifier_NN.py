from sklearn.datasets import load_iris                  # we'd like to use off-the-shelf data for demonstration
import numpy as np                                      # we'd like to calculate things with vectors
import pandas as pd                                     # we may need to use Pandas dataframe

## predefined values:
train_test_factor = 5 # 1/5 data would be used as testset

iris_raw = load_iris() # load the off-the-shelf iris data

# store the Iris information onto Pandas DataFrame
all_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris_data  = pd.DataFrame(data = np.c_[iris_raw['data'], iris_raw['target']], columns=all_columns) 


'''
Feature normalization:
    All the given features (sepal_length, sepal_width, petal_length, and petal_width) are given in float values, but not yet normalized. We'll apply scaling so that all values in a given feature would be in normal destribution form (mean=0 and standard-deviation=1)
'''
scaled_features = {}
for column in columns:
    # first, we'll obtain the value of mean and standard deviation
    mean, std = iris_data[column].mean(), iris_data[column].std()
    # second, we store those values in case original values are needed
    scaled_features[column] = [mean, std]
    # last, we'll update the original values by scaled values
    iris_data.loc[:, column] = (iris_data[column] - mean) / std

'''
Split data into training and testing:
    As we don't have the given data in training and testing partitions split. So we'll need to split them manually. 
'''
# We first shuffle the rows in iris dataframe with its index
iris_data = iris_data.sample(frac=1).reset_index(drop=True)
# We den decide the split index between training and testing partition
all_data_size = iris_data.shape[0] # number of records/rows in given iris data
train_test_split_index = int(1 / train_test_factor * all_data_size)
train_data_all = iris_data[train_test_split_index:]
test_data_all  = iris_data[:train_test_split_index]

X_train = train_data_all.iloc[:,0:4]
y_train = pd.get_dummies(train_data_all['target'], prefix='class')
X_test  = test_data_all.iloc[:,0:4]
y_test  = pd.get_dummies(test_data_all['target'], prefix='class')


'''
Sigmoid function: 
    given a vlaue (can be np vector) x, return (1 / 1+np.exp(x))
'''
def sigmoid(x):
    return(1 / 1 + np.exp(x))


'''
Mean Square Error function:
    given 2 set of values, return the value of mean square error
'''
def MSE(y, Y):
    return(np.mean(y-Y)**2)


'''
Neural Network class:
    define a newral-network class, where all the necessary / relevant functions (except sigmoid()) are contained
'''
class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # input_nodes:   number of input nodes
        # hidden_nodes:  number of hidden nodes
        # output_nodes:  number of output nodes
        # learning_rate: rate of the learning to be applied
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        # initialize the weights
        self.weights_input_hidden  = np.random.normal(0.0, self.hidden_nodes**-0.5, 
                                        (self.hidden_nodes, self.input_nodes))
        self.weights_hidden_output = np.random.normal(0.0, self.output_nodes**-0.5, 
                                        (self.output_nodes, self.hidden_nodes))

        # specify the activation function (sigmoid function in this case)
        self.activation_function = sigmoid

    def train(self, input_list, target_list):
        # convert the input list into 2-D (NumPy) array
        inputs  = np.array(input_list, ndmin=2).T
        targets = np.array(target_list, ndmin=2).T

        # forward pass
        #  calculate the output values of hidden layer
        hidden_inputs  = np.dot(self.weights_input_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        #  calculate the outputs value(s) of output layer
        final_inputs  = np.dot(self.weights_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # backward propergation
        #  calculate the errors in output layer
        output_errors = targets - final_outputs
        pass

    def run(self, input_list):
        pass


