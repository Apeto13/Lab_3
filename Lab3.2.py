


def find_largest_number(numbers):
    if not numbers:
        return None 
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number


listA = [1,2,1,4,5,7,3,9,90,5,76,98]
Max_number = find_largest_number(listA) 
print(Max_number)