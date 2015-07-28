Conditionals and For Loops
==========================

Get ready for FizzBuzz, again!

#### For Loop

For loop syntax in Python is slightly different.  
The 'for in' pattern is still available in Python:  
```
for thing in list:
	print(thing)
```
Python also has what's known as a range:
```
lst = ['a', 'b', 'c']
for i in range(len(lst)):
 	print(i)
0
1
2
```
If we wanted to print the element in the list, rather than the index, we could do it like this:  
```
lst = ['a', 'b', 'c']
for i in range(len(lst)):
 	print(lst[i])
a
b
c
```
With range, you have the option to choose the start and stop points, as well as increment.  
```
for i in range(2, 10, 2):
 	print(i)
2
4
6
8
```
As you can see, the end point is not included as part of the range.

Fire up your Python interpreter and try it out.

#### Conditionals - Switch

Switch statements are basically the same in Python. You can write if statements in two ways:
```
if(some condition):
	do something
```
or
```
if some condition:
	do something
```
for else clauses, it's also pretty similar.  
Here is an example:  
```
if condition:
	do something
elif another condition:
	do something else
else:
	catch all of the other possibilities
```

#### FizzBuzz

Time for FizzBuzz in Python.

Write code that does the following:  
* if i is divisible by 3, print "Fizz"
* if i is divisible by 5, print "Buzz"
* if i is divisible by 3 & 5, print "FizzBuzz"
* if i is not divisble by 3 or 5, print i
