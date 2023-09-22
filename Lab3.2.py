


def find_largest_number():
    numbers=[]
    for i in range(10):
        num = int(input("Enter The number: "))
        numbers.append(num)
    if not numbers:
        return None 
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num

    print(max_number)

find_largest_number()

