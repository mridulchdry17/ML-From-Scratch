import numpy as np

class Linear_Regression:
    def __init__(self,learning_rate = 0.01, n_iters = 1000):
        self.learning_rate = learning_rate  
        self.n_iters = n_iters
        self.W = 0
        self.b = 0

    def fit(self,X,y):
        for i in range(self.n_iters):
            n = len(y)
            y_predicted = self.W * X + self.b
            # Calculate Gradients 
            dw = (1/n) * np.sum((y_predicted - y) * X)
            db = (1/n) * np.sum(y_predicted - y)
            # Update Coefficients
            self.W -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self,X):
        return self.W * X + self.b
    
    def calculate_loss(self,X,y):
        y_predicted = self.W * X + self.b
        mse = np.mean((y_predicted - y) ** 2)
        return mse
    
# Example usage:
if __name__ == "__main__":
    # Example dataset
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])
    
    # Create and train model
    model = Linear_Regression(learning_rate=0.01, n_iters=1000)
    model.fit(X, y)
    
    # Predictions
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Loss calculation
    loss = model.calculate_loss(X, y)
    print("Loss (MSE):", loss)