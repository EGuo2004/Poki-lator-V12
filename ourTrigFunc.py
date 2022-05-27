pi = 3.14159265359 
#how close to 0 that it is treated as 0
radius_of_0 = 10**-10
import ourBaseFunc

def sin(x):
  x = x % (2*pi)
  output = 0
  for i in range(10):
    output += (((-1)**i)*(x**(2*i+1))) / (ourBaseFunc.factorial(2*i+1))
  return output

def cos(x):
  x = x % (2*pi)
  output = 0
  for i in range(10):
    output += (((-1)**i)*(x**(2*i))) / (ourBaseFunc.factorial(2*i))
  return output

def tan(x):
  denominator = cos(x);
  if denominator == 0: return None
  return sin(x)/ denominator

def csc(x):
  denominator = sin(x)
  if (denominator - 0 < radius_of_0): return None
  return 1/denominator

def sec(x):
  denominator = cos(x)
  if (denominator - 0 < radius_of_0): return None

  return 1/denominator

def cot(x):
  denominator = sin(x)
  if (denominator - 0 < radius_of_0): return None
  return(cos(x)/denominator)


def piExact(x):
  output = 3
  for i in range(1,x):
    output += 4*((-1)**(i-1)) / ((i*2) * (i*2+1) * (i*2+2))
  return output
  