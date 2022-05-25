# test time for algo
import time
import ourBaseFunc #Sqrt, Fac
#import ourTrigFunc
inital = time.time()
errorBound = 0.00001
print(ourBaseFunc.squareRoot(10, errorBound))
print(ourBaseFunc.factorial(5))
