import numpy as np

def gradient_descent_multivariate(X, y, lr=0.01, epochs=1000):
    X = np.hstack((np.ones((X.shape[0],1)), X))
    theta = np.zeros(X.shape[1])
    n = len(y)

    for _ in range(epochs):
        y_pred = X.dot(theta)
        error = y_pred - y
        gradient = (1/n) * X.T.dot(error)
        theta -= lr * gradient

    return theta

if __name__ == "__main__":
    X = np.array([[1, 2],
                    [2, 4],
                    [3, 6],
                    [4, 8],
                    [5, 10]])
    y = np.array([3, 6, 9, 12, 15])
    theta = gradient_descent_multivariate(X, y)
    print("Multivariate:", theta)

