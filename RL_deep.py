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
def cost_function(y,y_hat):
    j=0.5*sum((y-y_hat)**2)
    return j
#now we have to set the learning rate and the number of trainig iterations
alpha=0.01
num_iterations=5000
#Next we will start training the network 
cost=[]
for i in range(num_iterations):
    #we will perform the forward propagation and then we will predict the output 
    z1,a1,z2,y_hat=forward_prop(x,weight_ih,weight_ho)
    #next we will perform the backward propagation and then we will calculate the gradiants
    dj_dweight_ih,dj_dweight_ho=backward_prop(y_hat,z1,a1,z2)
    #next we have to update the weights using the learning rate alpha
    weight_ih=weight_ih-alpha* dj_dweight_ih
    weight_ho=weight_ho-alpha*dj_dweight_ho
    #next we have to compute the cost using the function created above named as cost_function
    c=cost_function(y,y_hat)
    #finally we have to store the calculated cost
    cost.append(c)
    
#If we want we can plot the cost function as follows 
plt.grid()
plt.plot(range(num_iterations), cost)
plt.title('Cost Function')
plt.xlabel('Training Iterations')
plt.ylabel('Cost')
