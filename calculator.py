def calculator(operation,num1,num2):
    switcher={
        'add':num1+num2,
        'subtract':num1-num2,
        'multiply':num1*num2,
        'divide':num1/num2
        if num2!=0
        else
        'Error:Division by Zero'
    }
    return switcher.get(operation,"Invalid Operation")
print(f"Addition of 10 and 5 : {calculator('add',10,5)}")
print(f"Subtraction of 10 and 5 : {calculator('subtract',10,5)}")
print(f"Multiplication of 10 and 5 : {calculator('multiply',10,5)}")
print(f"Division of 10 and 5 : {calculator('divide',10,5)}")
print(f"Division of 10 and 0 : {calculator('divide',10,0)}")
print(f"Modulus of 10 and 0 : {calculator('mod',10,0)}")