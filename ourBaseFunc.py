
params = {
    "squareRoot": [float],
    "factorial": [float],
    "e": [float],
    "ln":[float],
    "log":[float, float],
  }

def squareRoot(x, errorBound):
  #gives square root with 5 places of accuracy
  i = 1
  while((i+1)*(i*1) < x):
    i+=1
  #whole number close to x
  while(abs(x - (i * i)) > errorBound):
    i = (i + x/i)/2
  return i

def factorial(x):
  sum = 1
  for i in range(1,x+1):
    sum *= i
  return sum

def e(x):
  output = 0
  for i in range(50):
    output += (x**i)/factorial(i)
  return output

def ln(x):
  if(x == 0):
    return None
  else:
    output = 0
    for i in range(1,50):
      output += (((x-1) / (x+1)) ** (2*i-1))/(2*i-1)
    return (output * 2)

def log(base,value):
  return ln(value)/ln(base)

  
