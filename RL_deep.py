#importing the necessary libraries 
import numpy as np
import matplotlib.pyplot as plt
#next prepare the data

x = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
y = np.array([[1], [1], [0], [0]])
#next is to define the number of nodes in each layer 
num_input=2
num_hidden=5
num_output=1
#we will intitalize the weights and the bias randomly as follows
weight_ih=np.random.randn(num_input, num_hidden)
bias_ih=np.zeros((1,num_hidden))
#next we will initalize weight and bias from the input to the output layer
weight_ho=np.random.randn(num_hidden, num_output)
bias_ho=np.zeros((1,num_output))
#next we will define the sigmoid activation function 
def sigmoid(z):
    return 1/(1+np.exp(-z))
#next we will define the derivative of the sigmoid function
