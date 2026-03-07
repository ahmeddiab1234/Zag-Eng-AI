


def train_linear(X, y):
    print("Training Linear Regression model...")
    slope = sum(X) / len(X)
    intercept = 0.5
    return {"model": "LinearRegression", "slope": slope, "intercept": intercept}




