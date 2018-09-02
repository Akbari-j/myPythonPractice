
#3.11 Exercises

#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
#hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

#Exercise 2: Rewrite your pay program using try and except so that your program
#handles non-numeric input gracefully by printing a message and exiting the
#program. The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input


###################

hour = input ('insert your hour: ')
rate = input ('insert rate: ')
try:
    
    hour = float(hour)
    rate = float (rate)

    if hour <= 40:
        pay = hour * rate
    else:
        pay = (40 * rate) + (hour-40)*rate*1.5

    print(pay)
except:
    print("Please enter number!")
