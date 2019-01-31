import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def initialize_parameters(layers_dims, he=False):
    """ Initializes the weights of the network

    he = using he initialization method"""
    parameters = {}
    L = len(layers_dims)
    if he:
        for l in range(1, L):
            parameters["W" + str(l)] = np.random.randn(layers_dims[l], layers_dims[l-1]) * np.sqrt(2./layers_dims[l-1])
            parameters["b" + str(l)] = np.zeros((layers_dims[l], 1))
    else:
        for l in range(1, L):
            parameters["W" + str(l)] = np.random.randn(layers_dims[l], layers_dims[l-1]) * 0.01
            parameters["b" + str(l)] = np.zeros((layers_dims[l], 1))
    return parameters


def model(X, Y, layers_dims, optimizer, beta =0.9, beta1 = 0.9, beta2 = 0.09, 
          learning_rate = 0.03, num_epochs=5000, lambd=0, print_cost=True):
    """Runs the training of the network"""

    L = len(layers_dims)
    costs = []
    t = 0
    
    parameters = initialize_parameters(layers_dims, he=True)

    # if momentum initialize velocity
    if optimizer == "momentum":
        v = initialize_velocity(parameters)
    elif optimizer == "adam":
        v, s = initialize_adam(parameters)
    
    #Optimization Loop
    for i in range(num_epochs):
        AL, caches = L_model_forward(X, parameters)
        cost = compute_cost(AL, Y, parameters, lambd)
        grads = L_model_backward(AL, Y, caches, lambd)
        if optimizer == "momentum":
            parameters, v = update_parameters_with_momentum(parameters, grads, v, beta, learning_rate)
        elif optimizer == "adam":
            t += 1
            parameters, v, s = update_parameters_adam(parameters, grads, v, s, t, learning_rate, beta1, beta2)
        else:
            parameters = update_parameters(parameters, grads, learning_rate)
        # Print the loss every 250 iterations
        if print_cost and i % 250 == 0:
            print("Cost after iteration {}: {}".format(i, cost))
            costs.append(cost)
        
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('iterations (x250)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    return parameters


def linear_activation_forward(A_prev, W, b, activation):
    """Forward pass of one layer of the network"""
    
    def linear_forward(A_prev, W, b):
        Z = np.dot(W, A_prev) + b
        cache = (A_prev, W, b)
        return Z, cache

    Z, linear_cache = linear_forward(A_prev, W, b)

    if activation == "sigmoid":
        A = sigmoid(Z)
    elif activation == "relu":
        A = relu(Z)

    cache = (linear_cache, Z)

    return A, cache

def L_model_forward(X, parameters):
    """Forward pass of all the layers in network"""

    caches = []
    L = len(parameters) // 2
    A = X
    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(A_prev, parameters["W"+str(l)], parameters["b"+str(l)], activation="relu")
        caches.append(cache)

    AL, cache = linear_activation_forward(A, parameters["W"+str(L)], parameters["b"+str(L)], activation="sigmoid")
    caches.append(cache)

    return AL, caches


def linear_activation_backward(dA, caches, activation, lambd):
    """Backpropagation of one layer"""
    
    def linear_backward(dZ, cache, lambd):
        A_prev, W, b = cache
        m = A_prev.shape[1]
        dW = (1/m) * np.dot(dZ, A_prev.T) + lambd/m * W
        db = (1/m) * np.sum(dZ, axis=1, keepdims=True)
        dA_prev = np.dot(W.T, dZ)
  
        return dA_prev, dW, db

    linear_cache, activation_cache = caches

    if activation == "sigmoid":
        dZ = sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache, lambd)
    elif activation == "relu":
        dZ = relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache, lambd)

    return dA_prev, dW, db


def L_model_backward(AL, Y, caches, lambd):
    """Backpropagation of full network"""

    grads = {}
    L = len(caches) # Number of layers
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)

    dAL = -(np.divide(Y, AL) - np.divide(1-Y, 1-AL))

    # Lth Layer -> Sigmoid -> Linear
    current_cache = caches[L-1]
    grads["dA" + str(L-1)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL, current_cache, "sigmoid", lambd)

    for l in reversed(range(L-1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads["dA"+str(l+1)],
                                                                    current_cache, "relu", lambd)
        grads["dA"+str(l)] = dA_prev_temp
        grads["dW"+str(l+1)] = dW_temp
        grads["db"+str(l+1)] = db_temp
    
    return grads


def compute_cost(AL, Y, parameters, lambd):
    """Computes the loss of the model"""

    m = Y.shape[1]
    cross_entropy = -(1/m) * (np.dot(Y, np.log(AL.T)) + np.dot( 1 - Y, np.log(1-AL).T))
    L = len(parameters) // 2
    L2 = 0
    for l in range(L):
        L2 += np.sum(np.square(parameters["W" + str(l+1)]))
    L2 = lambd/(2*m) * L2

    cost = (cross_entropy + L2).reshape(1)
    cost = np.squeeze(cost)

    return cost

def update_parameters(parameters, grads, learning_rate):
    """Updates the weights of the network"""

    L = len(parameters) // 2
    for l in range(L):
        parameters["W" + str(l+1)] -= learning_rate * (grads["dW"+str(l+1)])
        parameters["b" + str(l+1)] -= learning_rate * (grads["db"+str(l+1)])
    return parameters


def relu(x):
    return x * (x > 0)

def relu_backward(dA, cache):
    """Backpropagation for a single RELU unit"""
    
    Z = cache
    dZ = np.array(dA, copy=True) # just converting dz to array
    
    # When z <= 0, dz = 0
    dZ[Z <= 0] = 0
    
    assert (dZ.shape == Z.shape)
    
    return dZ

def sigmoid(Z):
    """Sigmoid activation function"""
    
    A = 1/(1+np.exp(-Z))
    
    return A

def sigmoid_backward(dA, cache):
    """Backpropagation for a single Sigmoid unit"""
    
    Z = cache
    
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    
    assert (dZ.shape == Z.shape)
    
    return dZ

def predict(parameters, X):
    """Computes probabilities using forward propagation, and classifies to 0/1 using 0.5 as the threshold"""
    A2, cache = L_model_forward(X, parameters)
    predictions = (A2 > 0.6)

    return predictions

def initialize_velocity(parameters):
    """Initializes velocity for momentum"""
    L = len(parameters) // 2
    v = {}
    for l in range(L):
        v["dW"+str(l+1)] = parameters["W"+str(l+1)] * 0
        v["db"+str(l+1)] = parameters["b"+str(l+1)] * 0
    return v

def update_parameters_with_momentum(parameters, grads, v, beta, learning_rate):
    """Updates weights of network when it has momentum"""
    L = len(parameters) // 2
    for l in range(L):
        # update velocities
        v["dW"+str(l+1)] = beta * v["dW"+str(l+1)] + (1-beta) * grads["dW"+str(l+1)]
        v["db"+str(l+1)] = beta * v["db"+str(l+1)] + (1-beta) * grads["db"+str(l+1)]
        # update parameters
        parameters["W"+str(l+1)] -= learning_rate * v["dW"+str(l+1)]
        parameters["b"+str(l+1)] -= learning_rate * v["db"+str(l+1)]
    return parameters, v

def initialize_adam(parameters):
    """Initializes weights when optimization is with Adam method"""
    L = len(parameters) // 2
    v = {}
    s = {}
    for l in range(L):
        v["dW"+str(l+1)] = parameters["W"+str(l+1)] * 0
        v["db"+str(l+1)] = parameters["b"+str(l+1)] * 0
        s["dW"+str(l+1)] = parameters["W"+str(l+1)] * 0
        s["db"+str(l+1)] = parameters["b"+str(l+1)] * 0
    return v, s

def update_parameters_adam(parameters, grads, v, s, t, learning_rate, beta1=0.9, beta2=0.999, epsilon=1e-6):
    """Updates weights when optimization is with Adam method"""
    L = len(parameters) // 2
    v_corrected = {}
    s_corrected = {}

    for l in range(L):
        # moving average of gradients
        v["dW"+str(l+1)] = beta1 * v["dW"+str(l+1)] + (1-beta1) * grads["dW"+str(l+1)]
        v["db"+str(l+1)] = beta1 * v["db"+str(l+1)] + (1-beta1) * grads["db"+str(l+1)]
        # bias corrected first moment estimate
        v_corrected["dW"+str(l+1)] = v["dW"+str(l+1)] / (1 - beta1**t)
        v_corrected["db"+str(l+1)] = v["db"+str(l+1)] / (1 - beta1**t)
        # moving average of squared gradients
        s["dW"+str(l+1)] = beta2 * s["dW"+str(l+1)] + (1 - beta2) * np.power(grads["dW"+str(l+1)], 2)
        s["db"+str(l+1)] = beta2 * s["db"+str(l+1)] + (1 - beta2) * np.power(grads["db"+str(l+1)], 2)
        # bias corrected second raw movement estimate
        s_corrected["dW"+str(l+1)] = s["dW"+str(l+1)] / (1 - beta2**t)
        s_corrected["db"+str(l+1)] = s["db"+str(l+1)] / (1 - beta2**t)
        # upate parameters
        parameters["W" + str(l+1)] -= learning_rate * v_corrected["dW" + str(l+1)] / (np.sqrt(s_corrected["dW" + str(l+1)]) + epsilon)
        parameters["b" + str(l+1)] -= learning_rate * v_corrected["db" + str(l+1)] / (np.sqrt(s_corrected["db" + str(l+1)]) + epsilon)

    return parameters, v, s

def make_dev_set(X_train, Y_train, dev_size=80):
    """Builds the dev set"""

    permutations = list(np.random.permutation(X_train.shape[1]))

    X_train = X_train[:, permutations]
    Y_train = Y_train[:, permutations]
    X_dev = X_train[:, 0 : dev_size]
    X_train = X_train[:, dev_size:]
    Y_dev = Y_train[:, 0 : dev_size]
    Y_train = Y_train[:, dev_size:]

    return X_train, Y_train, X_dev, Y_dev

def print_predictions(parameters, ouput_file=True):
    """Prints predictions and outputs to csv file"""
    predictions = predict(parameters, X_train)
    print ('Train Accuracy: %d' % float((np.dot(Y_train,predictions.T) + np.dot(1-Y_train,1-predictions.T))/float(Y_train.size)*100) + '%')
    dev_predictions = predict(parameters, X_dev)
    print ('Dev Accuracy: %d' % float((np.dot(Y_dev,dev_predictions.T) + np.dot(1-Y_dev,1-dev_predictions.T))/float(Y_dev.size)*100) + '%')
    test_predictions = predict(parameters, X_test)
    output = pd.DataFrame({ 'Id' : test_ids, 'Y': test_predictions.reshape(-1,)*1 })
    output.to_csv('output.csv', index=False)


def start_network(X_train, Y_train, X_test, Y_test, layer_dims=[X_train.shape[0], 5, 5, 1]):
    """Starts the model"""
    X_train, Y_train, X_dev, Y_dev = make_dev_set(X_train, Y_train)
    parameters = model(X_train, Y_train, layers_dims, optimizer="adam", beta=0.9, beta1=0.9, beta2=0.999, 
          learning_rate = 0.0005, num_epochs=10000, lambd=0.015, print_cost=True)
    print_predictions(parameters)  


