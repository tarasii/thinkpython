#endles generators
def fibonaccy_generator():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
        
def factorial_generator():
    i = 1
    a = 1
    yield a
    while True:
	     i +=1
	     a = a * i
	     yield a
        
        
