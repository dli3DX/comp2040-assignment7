from math import sqrt

class LinRegModel:
    def __init__(self, slope=0, bias=0):
        self.slope = slope
        self.bias = bias

    def __repr__(self):
        return f"*** Model parameters: slope = {self.slope}, bias = {self.bias} ***"

    def predict(self, x):
        return [self.slope * xi + self.bias for xi in x]

def rmse(yhat, y):
    return sqrt(sum((p - a) ** 2 for p, a in zip(yhat, y)) / len(yhat))
