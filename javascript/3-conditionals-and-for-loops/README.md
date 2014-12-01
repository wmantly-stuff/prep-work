####Conditionals and For Loops

Get ready for FizzBuzz!

This is a classic programming test - that yes, you will actually see at job interviews.

It basically just checks if you can write a for loop and if you know what [modulo](http://en.wikipedia.org/wiki/Modulo_operation) is.

###For Loop

This is the most basic loop we write in Javascript, and most languages for that matter. The ubiquitous For Loop.

		for(var i = 0; i<=100; i++){ console.log(x) }

In the first argument, we declare an incrementing variable, i, and where it will start. We could have called it anything.

In the second argument, we state the conditions under which the following code should be executing. In this case, it is while i is less than or equal to 100.

In the third argument, we say that every time the code is run, i should increment by 1. i++ is shorthand, also known as [syntactic sugar](http://en.wikipedia.org/wiki/Syntactic_sugar) for i += 1, or  i = i + 1. They all do the same thing. 

To get a slightly different view of it, we could do it this way.

		for(var x = 500; x > 150; x-=5){ console.log(x) }

Try it in your browser or node console and watch it work. What is the last number it prints? Why?

###Conditionals - If / Else

The most simple conditional statement is the if statement. This is also ubiquitous across many programming languages.

Basically it is written like this:

if(some condition){
	do this
}

You can make it more powerful by specifying an else. This is a catch all for things to do if the first condition isnt met. For example:

if(cute store clerk has brown hair){
	give phone number
} else {
	leave store
}

Finally, we can specify multiple outcomes using an else if. 

if(cute clerk has brown hair){
	give phone number
} elseif(cute clerk has blond hair) {
	get phone number
} else {
	buy playstation
}

Instead of this plain english example, also known as [Pseudocode](http://en.wikipedia.org/wiki/Pseudocode)

Get the idea?

###Fizzbuzz

Ok, now onto FizzBuzz.

Open the main.js file and find the loop inside the document ready.

Write code that does the following:

if i is divisable by 3, append a line that reads "Fizz" 

if i is divisable by 5, append a line that reads "Buzz"

if i is divisable by 3 & 5, append a line that reads "FizzBuzz"

All this should be done as usual, to the printout div.