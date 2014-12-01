Bank Accounts 2
===============

In this assignment, you will be taking your code from Bank Accounts 1 and applying it to the DOM.  
This is not an easy assignment. Work together and ask for help.  
* Take a look through the code and see what you've been given so far. There is a modal ready to use in the html. You will be using it later in the assignment.  
* You have a form on the left to create a bank account. Make a bank account object using the inputs from the form.
* Append the bank account name to the 'Bank Accounts' list.
* When you click on the name of a bank account, it should show the modal, and hide the container.
* In the modal, show the user's account name and balance in their respective divs (given to you in the html)
* Use the deposit and withdrawal forms to do their respective functions to the bank account.
* Upon deposit, withdrawal, or 'I'm done', hide the modal, and show the container again.
* _stretch_: When the modal pops up, rather than hiding the container, make it fall to the background and be less visible (opacity, visibility, color... your choice). Add error checking. Clear the forms after submit. See if there is any other functionality you think this page should have. Show off.  

Here is some code to create account numbers:  
```
this.accountNumber = (Math.floor(Math.random() * (9999999999 - 1000000000)) + 1000000000).toString()
```
