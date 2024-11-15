#create a program if numbers are multiplied together and equal less than 1000 then multiply 
#otherwise add
def multi_or_add(num1, num2):
#calculate the product or number 

    calculation = num1 * num2

    if calculation <=1000:
        return f"the result was multiplied: {calculation}"
    else:
        return f"the result was added: {num1 + num2}"
    
result = multi_or_add(20,30)
print("result is: ", result)

result = multi_or_add(3,40)
print("result is: ", result)
