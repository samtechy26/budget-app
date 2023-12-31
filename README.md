# Budget App
A simple budget application created using python applying OOP.

Created a  Category class in budget.py. It is able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. 

The class contains the following methods:

A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
A withdraw method that is similar to the deposit method, but the amount passed in is stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method returns True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method is used by both the withdraw method and transfer method.

When the budget object is printed it  displays:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line shows the description and amount. The first 23 characters of the description is displayed, then the amount. The amount is right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, there is a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It returns a string that is a bar chart.

The chart shows the percentage spent in each category passed in to the function. The percentage spent is calculated only with withdrawals and not with deposits. Down the left side of the chart are labels 0 - 100. The "bars" in the bar chart is made out of the "o" character. The height of each bar is been rounded down to the nearest 10. The horizontal line below the bars goes two spaces past the final bar. Each category name is written vertically below the bar. There is a title at the top that says "Percentage spent by category".

This function is tested with up to four categories.

example output

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
The unit tests for this project are in test_module.py.