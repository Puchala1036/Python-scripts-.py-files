# Factorial Using a Function 
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

number=5
total=fact(number)
print(total)

import math

#Math Module for Calculations

number = float(input("Enter a number: "))


sqrt_value = math.sqrt(number)
log_value = math.log(number)        
sine_value = math.sin(number)       

print(f"Square root of {number} is: {sqrt_value}")
print(f"Natural logarithm (log base e) of {number} is: {log_value}")
print(f"Sine of {number} radians is: {sine_value}")