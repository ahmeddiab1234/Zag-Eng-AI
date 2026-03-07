import numpy as np

def gradient_descent_bivariate(x1, x2, y, lr=0.01, epochs=1000):
    weight1, weight2, bias = 0.0, 0.0, 0.0
    n = len(y)

    for _ in range(epochs):
        y_pred = bias + weight1 * x1 + weight2 * x2
        error = y_pred - y

        d_bias = (1/n) * np.sum(error)
        d_weight1 = (1/n) * np.sum(error * x1)
        d_weight2 = (1/n) * np.sum(error * x2)

        weight1 -= lr * d_weight1
        weight2 -= lr * d_weight2
        bias -= lr * d_bias

    return weight1, weight2, bias

if __name__ == "__main__":
    # y = 0 + 1*x1 + 1*x2
    x1 = np.array([1, 2, 3, 4, 5])
    x2 = np.array([2, 4, 6, 8, 10])
    y = np.array([3, 6, 9, 12, 15])  
    weight1, weight2, bias = gradient_descent_bivariate(x1, x2, y)
    print("Bivariate: weight1 =", weight1, ", weight2 =", weight2, ", bias =", bias)


# y = w1*x1 + w2*x2 + b