def largest_num(num_list):
    if (len(num_list)) == 0:
        print("the list is empty")
        return True
    else:
        print("the list is not empty")
    large_num = num_list[0]
    for num in num_list:
        if num > large_num:
           large_num = num
    return large_num

numbers = [10, 30, 60, 20, 100, 160, 120]
largest = largest_num(numbers)
print("largest number is", largest)


#  without using the function

num1 = [10, 20, 40, 80, 20]
large_number = num1[0]
for numb in num1:
     if numb > large_number:
        large_number = numb
print("the largest number is", large_number)

