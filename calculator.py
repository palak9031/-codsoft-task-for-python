# basic calculator using python

#taking one no.2

a = int ( input("Enter the first number"))
#taking another no.
b = int(input("Enter the second number"))
#choosing our operations
operators = input("Enter the operators type (+,-,*,/): ")

result = 0

#applying condition for loops
if operators  == "+":
    result = a + b
                    
 
elif operators == "-":
   result = a - b
                    
 
elif operators == "*":
    result = a * b
                    
 
elif operators == "/":
   result = a / b
                    
else:
    print("Invalid input")

print("your answer is: " , result)
