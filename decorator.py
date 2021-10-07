import time

def fib_decorator(func):
    def wrapper():
      start=time.perf_counter()
      print("start time: ",start)
      value=func()
      end = time.perf_counter()
      runtime = end-start
      print("end time: ",end)
      print("time taken : ", runtime)
      return value
    return wrapper

@fib_decorator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f=fib()
print("---------------------------")
n=int(input('enter value for n : '))
for i in range(n):
    print(next(f))