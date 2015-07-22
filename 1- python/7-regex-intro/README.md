Regular Expressions
===================

Regular Expressions (regex for short) are a way to represent patterns in strings. They aren't as bad as people make them out to be. When used on the right problem, they are a great solution.

Go to [Rubular](http://rubular.com/). We're going to sandbox inside it a bit to get acquainted with regex syntax. At the bottom of the page is a regex cheat sheet.  
Note: Depending on the language, you may have to escape certain characters. For example, instead of `a{3}`, you may have to type `a\{3\}`.  
Also, be careful with periods (`.`). A period means any character in regex, so you have to escape it if you want to pattern match a period.

Here are some examples of regex and matching string patterns:  
* `a{3}` => `aaa`
* `a{3,}` => `aaaaaaaa`
* `[a-z]` => any lowercase letter
* `[A-Z]{4,6}` => between 4 and 6 uppercase letters, ex. `FASDV`
* `.` => any character
* `\w\.` => `_.`
* `hello\d?` => `hello` or `hello5`
* `[a-nO-Z]*` => abcOZZ

Make a regex to match each of these strings:  
* match 'byte academy' 3 different ways
* an 8 character password, do not allow non word characters
* an 8 character password that has at least 1 number and 1 capital letter


* byteacademy@example.com
* byte.academy@example.com
* byteacademy22@example.co.uk  
See if you can get all three with 1 regex, but not invalid emails (not having an @, etc...)
