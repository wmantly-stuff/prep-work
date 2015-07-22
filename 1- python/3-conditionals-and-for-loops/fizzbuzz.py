def fizzbizz(num):
    pass


def assertion(actual, expected):
    print(str(actual) + " == " + str(expected) + " : " + str(actual==expected))

assertion(fizzbuzz(33), "Fizz")
assertion(fizzbuzz(20), "Buzz")
assertion(fizzbuzz(30), "FizzBuzz")
assertion(fizzbuzz(32), 32)
