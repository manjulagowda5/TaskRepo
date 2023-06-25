def sum_of_all_numbers(numbers):
    total = 0
    for num in numbers:
      total += num
    return total

sum_list = [10, 20, 5, 40, 50]
sum_of_numbers = sum_of_all_numbers(sum_list)
print(sum_of_numbers)
