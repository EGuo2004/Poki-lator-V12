def gcd(a, b):
  while (b != 0):
      t = b
      b = a % b
      a = t
  return a

def lcm(a,b):
  return (a * b)/gcd(a,b)

def mean(arr):