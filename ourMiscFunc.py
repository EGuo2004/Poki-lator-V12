import ourBaseFunc as BF
def gcd(a, b):
  while (b != 0):
      t = b
      b = a % b
      a = t
  return a

def lcm(a,b):
  return (a * b)/gcd(a,b)

def mean(arr):
  sum = 0
  for i in range(len(arr) + 1):
    sum += arr[i]
  return sum/len(arr)

def median(arr):
  center = len(arr)/2
  if (len(arr) % 2 == 0):
    return (arr[center] + arr[center + 1])/2
  else:
    return arr[center + 0.5]

def nCr(n,r):
  return (BF.factorial(n))/(BF.factorial(r) * BF.factorial(n-r))

def nPr(n,r):
  return (BF.factorial(n))/(BF.factorial(n-r))