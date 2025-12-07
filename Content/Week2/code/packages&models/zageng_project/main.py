from models.regression.linear_regression import train_linear
from models.regression.ridge_regression import train_ridge
from models.classification.svm import train_svm
from models.classification.decision_tree import train_tree

X = [1, 2, 3, 4]
y = [2, 4, 6, 8]

linear_model = train_linear(X, y)
ridge_model = train_ridge(X, y, alpha=0.5)

svm_model = train_svm(X, y)
tree_model = train_tree(X, y)

print("\n--- Model Summary ---")
print(linear_model)
print(ridge_model)
print(svm_model)
print(tree_model)
