def fibonacci(num):
	pass



# TESTS
import random
def random_fibonacci():
	fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
	return random.sample(fib, 1)[0]

assert(fibonacci(random_fibonacci()) == True), "Random Fibonacci number should return true"
assert(fibonacci(50) == False), "50 should return false"
assert(fibonacci(97450) == False), "50 should return false"
assert(fibonacci(1) == True), "1 should return true"
assert(fibonacci(7540113804746346429) == True), "A massive number in sequence should return true"
