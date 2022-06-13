def ValidateTrig(x):
    print(type(x))
    if type(x).__name__ != 'float':
      raise ValueError("x must be float")