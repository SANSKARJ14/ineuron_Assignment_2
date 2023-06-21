# ASSINGMENT2
"""
1.What are the two values of the Boolean data type? How do you write them?

The two values of the Boolean data type are True and False.
In Python, these values are represented as keywords and are written exactly as shown,
with the first letter capitalized."""


"""
2. What are the three different types of Boolean operators?

the three boolean operators are (or, not , and) these are 3 boolean operator 
"""

"""
3. Make a list of each Boolean operator truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

not 
|  | Result |

|  False  |  True  |
|  True   | False  |

or 
| 1         |         2 | Result |

|   False   |   False   | False  |
|   False   |   True    | True   |
|   True    |   False   | True   |
|   True    |   True    | True   |

and 
|  1        |     2     | Result |

|   False   |   False   | False  |
|   False   |   True    | False  |
|   True    |   False   | False  |
|   True    |   True    | True   |
"""
"""
4. What are the values of the following expressions?

-(5 > 4) and (3 == 5)

Value: False
Explanation: The expression (5 > 4) evaluates to True, and (3 == 5) evaluates to False.
Since one of the operands is False, the overall expression evaluates to False.

-not (5 > 4)

Value: False
Explanation: The expression (5 > 4) evaluates to True.  so it becomes False.

-(5 > 4) or (3 == 5)

Value: True
Explanation: The expression (5 > 4) evaluates to True, and (3 == 5) evaluates to False.
The or operator returns True if at least one of the operands is True. Since one of the operands is True, 
the overall expression evaluates to True.

-not ((5 > 4) or (3 == 5))

Value: False
Explanation: The expression (5 > 4) or (3 == 5) evaluates to True. 
The not operator negates the value, so it becomes False.

-(True and True) and (True == False)

Value: False
Explanation: The expression (True and True) evaluates to True, and (True == False) evaluates to False. 
The and operator returns True only if both operands are True. Since one of the operands is False, 
the overall expression evaluates to False.

-(not False) or (not True)

Value: True
Explanation: The expression not False evaluates to True, and not True evaluates to False. T
he or operator returns True if at least one of the operands is True. Since one of the operands is True,
the overall expression evaluates to True.
These are the resulting values when evaluating each of the given expressions.
"""

"""
5. What are the six comparison operators?

The six comparison operators in Python are:

Equal to (==): Checks if two values are equal.
Example: 5 == 5 returns True.

Not equal to (!=): Checks if two values are not equal.
Example: 5 != 3 returns True.

Greater than (>): Checks if the left is greater than the right .
Example: 5 > 3 returns True.

Less than (<): Checks if the left  is less than the right .
Example: 3 < 5 returns True.

Greater than or equal to (>=): Checks if the left is greater than or equal to the right .
Example: 5 >= 5 returns True.

Less than or equal to (<=): Checks if the left  is less than or equal to the right .
Example: 3 <= 5 returns True.
"""

""" 
6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

to differentiate between the equal to (==) operator and the assignment (=) operator in Python, consider the following:

Equal to Operator (==):

The equal to operator (==) is used for comparison to check if two values are equal.
It returns True if the values on both sides of the operator are equal and False otherwise.
Example: x == y compares the values of x and y and returns True if they are equal.

Assignment Operator (=):

The assignment operator (=) is used to assign a value to a variable.
It assigns the value on the right side of the operator to the variable on the left side.
Example: x = 5 assigns the value 5 to the variable x.
A condition is a statement that evaluates to either True or False and is commonly used in control flow structures 
like if statements and loops. When working with conditions,
you would use the equal to operator (==) to compare values and determine if a certain condition is satisfied.

For example,
x = 5
if x == 5:
    print("The value of x is 5.")
"""
"""
7. Identify the three blocks in this code:

the 3 blocks are 
1-if spam == 10:
    print('eggs')
2-if spam > 5:
    print('bacon')
3-else:
    print('ham')
print('spam')
print('spam')
"""
"""
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
"""
spam = int(input("what is the spam value"))
if spam == 1:
    print ("hello")
elif spam == 2 :
    print ("howdy")
else:
    print("greating")

""" 9.If your programme is stuck in an endless loop, what keys you’ll press?
we will press Ctrl + C 
"""
"""10. How can you tell the difference between break and continue?
break is used to terminate the loop entirely, while continue is used to skip the rest of the current iteration and
move to the next iteration of the loop.

example 
         for i in range(5):
            if i == 2:
               continue 
            print (i)  ruselt will bw 0,1,3,4,5
example 2               
          for i in range(5):
            if i == 2:
               break 
            print (i)  ruselt will bw 0,1   
"""
"""11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

all three expressions range(10), range(0, 10), and range(0, 10, 1) generate the same sequence of numbers from 0 to 9
(inclusive) with a step size of 1. They differ only in the way the parameters are specified, 
where the start value, stop value, and step size can be explicitly provided.(start value , spot value , step size)
"""

"""12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop"""

for i in range(11):
    print (i)

i = 0
while i <= 10:
    print (i)
    i = i + 1

"""13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

spam.bacon()
"""


















































































































