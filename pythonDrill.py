# 1. Assign an integer to a variable
integer = 3
print(integer)
# 2. Assign a string to a variable
string = "my string"
# 3. Assign a float to a variable
float=355/113
print(float)
'''
4. Use the print function and
.format() notation to print out
the variable you assigned
'''
print("{} is my float number".format(float))
# 5. Use each of these operators +, - , * , / , +=, ­= , %
plus = 33+44
minus = 11-58
multiply = 43*37
divide = 22/7
number = 5
number += divide
print(number)
number -= float
print(number)
modulo=plus%10
print(modulo)
# 6. Use of logical operators: and, or, not
number1=3
number2=8
number3=29
if type(number1) and type(number2) and type(number3)==int:
  print("they are int types")
if number1%2==0 or number2%2==0 or number3%2==0:
  print("there is an even number")
if not number3%2==0:
  print(str(number3)+" is not even")
# 7. Use of conditional statements: if, elif, else

if number1>9 and number2>9 and number3>9:
  print("they are all positive two digit numbers")
elif number1%2==0 and number2%2==0 and number3%2==0:
  print("they are all positive even numbers with different numbers of digits")
else:
  print("they are positive numbers with different numbers of digits, and are not all even or odd")

# 8. Use of a while loop
x=0
while x<=12:
  print("while loop counting: " + str(x))
  x+=1
# 9. Use of a for loop
for x in range (0,13):
  print("for loop counting: " + str(x))
# 10. Create a list and iterate through that list
#using a for loop to print each item out on a new line
list=["a",1,"b",2,"c",3,"d",4,"e",5]
for item in list:
  print ("list print: " + str(item))
# 11. Create a tuple and iterate through it using a
# for loop to print each item out on a new line
tuple=("a",1,"b",2,"c",3,"d",4,"e",5)
for item in tuple:
  print ("tuple print: " + str(item))

# 12. Define a function that returns a string variable
# 13. Call the function you defined above and print the result to the shell  

def myFunction():
  myString = "my string variable"
  print(myString)
  return(myString)

myFunction();

  



