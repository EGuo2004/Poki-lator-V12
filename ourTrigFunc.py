pi = 3.14159265359 
import ourBaseFunc

def sin(x):
  sum = 0
  for n in range(10):
    ((-1)**n * x**(2 * n))/(2)
  pass

def cos(x):
  x = x % (2*pi)
  output = 0
  for i in range(10):
    output += ((-1)**i)*(x**(2i))/(fact(2*i))
 print(output)

def tan(x):
  pass

def csc(x):
  pass

def sec(x):
  pass

def cot(x):
  pass