Reverse Polish Notation
=======================

You've never done it until you've done it reverse polish.

I don't know what that means, but check this out on [reverse polish notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Reverse polish notation is a mathematical notation in which every operator follows all of its operands. For example:

	3 4 + >>> 7  
	4 2 / >>> 2  
	10 7 2 - * 5 / >>> 10

Write a program that accepts a RPN equation as a command line argument, such that you would execute your program:

		python3 rpn_calc.py 10 9 - 5 +

Which would then return you 6, the result of that equation.

###ARGV

To run the program like this you need to import the sys library and access sys.argv. 

ARGV gives us the arguments used to launch the program as an array. The first position is always the application name / file. The next are all others divided by spaces.

Read about sys.argv [here](http://www.pythonforbeginners.com/system/python-sys-argv)

Sandbox with this so you know what you are getting as an input.

Here's a nice hint - we can "slice" arrays in Python like in JS just by doing:

		array = ['hi', 'wut', 'm8', 'lol', 'doge']
		array[2:4] ### returns ['m8', 'lol']

###Testing

Write some assert statements after you've solved the challenge.

NOTE: You might need to escape the multiplication operator * when you pass it in. 
