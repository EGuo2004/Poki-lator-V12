params = {
  "arctan": [float],
  "arcsin": [float],
}

broken = {
  "arcsin":None,
}

#x, y
#x: value that we want to find theta for
#y: to what degree of specifity
def arctan(x,y=5):
  error_bound = 10**(-1 * abs(y))
  sum = 0
  #because alternating series, next term is the error_bound
  next_term = error_bound + 1 
  n = 0 
  while (abs(next_term) > error_bound):
    sum += next_term
    next_term = (-1)**n *(x)**(2*n+1)
    next_term /= 2*n+1
    n+=1
  return sum


def arcsin(x, y=5):
  error_bound = 10**(-1 * abs(y))
  sum = 0
  while (True):
    pass


  