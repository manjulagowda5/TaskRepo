def factorial(number):
    if number < 0:
        return None  # Factorial is undefined for negative numbers
    elif number == 0:
        return 1  # Factorial of 0 is 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

num = 10
factorial_num = factorial(num)
if factorial_num is not None:
    print("The factorial of", num, "is", factorial_num)
else:
    print("Factorial is undefined for negative numbers.")
