from ourCalcFuncHelper import calculateFunction
num_of_steps = 100

params = {
  "nDerivative": [str],
  "RiemannSum": [str, str, int, int], 
  "TrapezoidalSum": [str, int, int],
  "euler": [str, int, int],
  "zerofinder": [str, int, int, int]
}

broken = {
  "euler":None,
  "zerofinder": None,
  "calculateFunction":None,
}

def nDerivative(function, x):
  errorBound = 10 ** -5
  Big = calculateFunction(function,x+errorBound)
  Small = calculateFunction(function,x)
  return (Big-Small)/errorBound

def RiemannSum(function, direction, start, end):
  stepsize = (end-start)/num_of_steps
  val = 0
  if(direction == 'left'):
    for i in range(start,end,stepsize):
      val += stepsize * calculateFunction(function,i)
  elif(direction == 'right'):
    for i in range(start+stepsize,end+stepsize,stepsize):
      val += stepsize * calculateFunction(function,i)
  elif(direction == 'middle'):
    for i in range(start,end,stepsize):
      val += stepsize * calculateFunction(function,(2*i+stepsize)/2)
  else:
    return None
  return val
 


def TrapezoidalSum(function, start,end):
  stepsize = (end-start)/num_of_steps
  sum = 0
  cur_x = start
  while (cur_x < end):
    averageVal = (calculateFunction(function, cur_x) + calculateFunction(function, cur_x+num_of_steps)) / 2
    sum += averageVal * stepsize
    cur_x += stepsize
    return sum

def euler(function,start,end):
  yval = 0
  stepsize = (end-start)/num_of_steps
  for i in range(start,end+stepsize):
    pass
    #Needs work plz harp
    #yval = yval + stepsize * 
  return None 

# returns x value of 0
def zerofinder(function, left, right, guess):
  general_steps = num_of_steps / 2
  leftstep = (left - guess)/general_steps
  rightstep = (right - guess)/general_steps
  cur_left = guess
  cur_right = guess
  guessIsPos = calculateFunction(function, guess) < 0 
  temp = None
  for i in range(num_of_steps):
    cur_left += leftstep
    cur_right += rightstep
    temp = (calculateFunction(function, cur_left), cur_left)
    if guessIsPos != temp < 0: break
    temp = (calculateFunction(function, cur_right), cur_right)
    if guessIsPos != temp < 0: break
  if temp == None:
    print(temp)

    # squeeze theorm using num_of_steps
    #to find the 0
  return temp
  # refine temp more, by the steps
