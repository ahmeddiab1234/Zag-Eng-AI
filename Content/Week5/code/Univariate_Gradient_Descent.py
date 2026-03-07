import numpy as np

def gradient_descent_univariate(x, y, lr=0.01, epochs=1000):
    weight = 0.0 
    bias = 0.0 
    n = len(x)

    for _ in range(epochs):
        y_pred = bias + weight * x
        error = y_pred - y

        d_weight = (1/n) * np.sum(error * x)
        d_bias = (1/n) * np.sum(error)

        weight = weight - lr * d_weight
        bias = bias - lr * d_bias

    return weight, bias

if __name__ == "__main__":
    # y = 1 + 2*x
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 7, 9, 11]) 
    weight, bias = gradient_descent_univariate(x, y)
    print("Univariate: weight =", weight, ", bias =", bias)


