def squareRoot(x, errorBound):
  #gives square root with 5 places of accuracy
  i = 1
  while((i+1)*(i*1) < x):
    i+=1
  #whole number close to x
  while(abs(x - (i * i)) > errorBound):
    i = (i + x/i)/2
  return i