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