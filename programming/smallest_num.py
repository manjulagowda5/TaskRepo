def smallest_number(number):
    if (len(number)) == 0:
        print("the list is empty")
    else:
        smallest = num_list[0]
        for num in num_list:
            if num < smallest:
                smallest = num
    return smallest


num_list = [10, 5, 70, 60, 20]
small_number = smallest_number(num_list)
print("the smallest number", small_number)
