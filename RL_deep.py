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
def sigmoid_derivative(z):
    return np.exp(-z)/((1+np.exp(-z)**2))
#next we will define the forward propagation
def forward_prop(x,weight_ih,weight_ho):
    z1=np.dot(x,weight_ih)+bias_ih
    a1=sigmoid(z1)
    z2=np.dot(a1,weight_ho)+bias_ho
    y_hat=sigmoid(z2)
    return z1,a1,z2,y_hat
#next we will define the backward propagation
def backward_prop(y_hat,z1,a1,z2):
    delta2=np.multiply(-(y-y_hat),sigmoid_derivative(z2))
    dj_dweight_ho=np.dot(a1.T, delta2)
    delta1=np.dot(delta2,weight_ho.T)*sigmoid_derivative(z1)
    dj_dweight_ih=np.dot(x.T,delta1)
    return  dj_dweight_ih, dj_dweight_ho
#next we will define the cost function 
