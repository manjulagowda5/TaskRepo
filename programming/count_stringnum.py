def count_string(strings):
    count = 0
    for string in strings:
        # isinstance(string, str) is converting the string 
        if isinstance(string, str) and len(string) >= 2:
            count += 1
    return count

string_list = ['apple','a','mango',1,'cow','papaya']
count = count_string(string_list)
print(count)

