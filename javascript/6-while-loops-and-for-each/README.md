####While and For Each Loops

In this challenge, we're going to write a while loop, a For In loop, and nest them.

###While Loops

A while loop iterates until a condition is no longer true. For example:

		while(greg == alive){
			live_year(1)
			age++
		}

Seemingly, a while loop could be endless. In that case, we have to break it. Take the following example:
		
		i = 0

		while(true){
			i++
			print("I'm an endless loop")
			if(i >= 50){
				break;
			}
		}

This will run exactly 50 times.

###For In

A For In loop iterates through each index in the data structure. In an array, an index is an integer, that starts at 0. Take this example:

		var array = ['john', 'bobby', 'homa', 'stevie', 'rob']

		for(var i in array){
			console.log(i) // prints 0, 1, 2, 3, 4
		}

In an object however, the index is a string. Check this out:

		var obj = {'john': 'student', 'bobby': 'programmer', 'homa': 'actress', 'stevie': 'gamer'}

		for(var k in obj){
			console.log(k) // prints 'john', 'bobby', 'homa', 'stevie'
		}

###Sandbox

Try this on your own in your node console or browser console. Declare some objects, iterate through them, print them out.

Also check out [.forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

###Multiplication Tables

Using any loop / loops of your choosing, write code that prints the multiplication tables up to a number input by the user in a form.

Create the form that gets the user input yourself above the #printout div, and append the result to the printout div.

Bonus if you actually use a table.

Your return should look something like this:

		// userinput = 7

0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |  
1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |  
2 | 2 | 4 | 6 | 8 | 10| 12| 14|  
3 | 3 | 6 | 9 | 12| 15| 18| 21|  
4 | 4 | 8 | 12| 16| 20| 24| 28|  
5 | 5 | 10| 15| 20| 25| 30| 35|  
6 | 6 | 12| 18| 24| 30| 36| 42|  
7 | 7 | 14| 21| 28| 35| 42| 49|   

