def multiply_number(number):
    multiply = 1
    for mult in num_list:
        multiply = mult * multiply
    return multiply

num_list = [10,20,30]
mult_all = multiply_number(num_list)
print(mult_all)
