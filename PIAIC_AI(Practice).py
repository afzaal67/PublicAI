
#Assignment 1
#Simple Calculator
#Afzaal Ahmed
#RollNo. PIAIC138345
operator=input('''please select math operator to perform:
+ for addition
- for subtraction
/ for division
* for multiplication''')

fNo=int(input("please enter first no:   "))
sNo=int(input("please enter second no:   "))

if operator=='+':
    print("Result is :",fNo+sNo)

elif operator=='-':
    print("Result is :",fNo-sNo)

elif operator=='/':
    print("Result is :",fNo/sNo)

elif operator =="*":
    print("Result is :",fNo*sNo)

