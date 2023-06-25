def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter the number:"))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
