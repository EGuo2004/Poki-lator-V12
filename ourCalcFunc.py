def nDerivative(function, x):
  errorBound = 10 ** -5
  xhfunc = ''
  xfunc = ''
  Big = calculateFunction(function,x+errorBound)
  Small = calculateFunction(function,x)
  return (Big-Small)/errorBound

def RiemannSum(function, direction, start, end):
  stepsize = (end-start)/100
  val = 0
  if(direction == 'left'):
    for i in range(start,end,stepsize):
      val += stepsize * i
  if(direction == 'right'):
    for i in range(start+stepsize,end+stepsize,stepsize):
      val += stepsize * i
  return val
    

#calculate function 
#@param 
def calculateFunction(function, x):
  # special st
  specialStrings = [['(', ')'

