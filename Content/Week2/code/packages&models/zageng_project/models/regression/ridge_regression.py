

def train_ridge(X, y, alpha=0.1):
    print(f"Training Ridge Regression model with alpha={alpha}")
    weight = sum(X) / (len(X) + alpha)
    return {"model": "RidgeRegression", "weight": weight, "alpha": alpha}




