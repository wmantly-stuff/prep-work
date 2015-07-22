While Loops in Python
=====================

A while loop iterates until a condition is no longer true. For example:
```
i = 0
while i < 10:
	print(i)
	i += 1
```
Be careful with while loops. If your while loop doesn't have a way to end, it will go on until it crashes.
```
i = 10
while i > 5:
	print(i)
	i += 1
```

#### Multiplication Tables

Using any loop / loops of your choosing, write code that prints the multiplication tables up to a number

Your return should look something like this:  
```
# userinput = 7

0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |  
1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |  
2 | 2 | 4 | 6 | 8 | 10| 12| 14|  
3 | 3 | 6 | 9 | 12| 15| 18| 21|  
4 | 4 | 8 | 12| 16| 20| 24| 28|  
5 | 5 | 10| 15| 20| 25| 30| 35|  
6 | 6 | 12| 18| 24| 30| 36| 42|  
7 | 7 | 14| 21| 28| 35| 42| 49|
```
Python does not change data types for you. If you would like to mix an integer and "|" into a string, you have to explicitly change the integer into a string. the method str() will do this for you.
```
1 + "c" # this won't work
str(1) + "c" # this will be "1c"
```
