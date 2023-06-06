def bank(X, Y):
    sum = X * (1 + 0.1)**Y
    return sum
print(bank(1000, 10))