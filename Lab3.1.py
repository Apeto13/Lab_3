


def Store():
    global dict_emp
    dict_emp = {}
    name = input("Enter the name of the employee: ")
    salary = input("Enter the salary of that employee: ")
    while(name != 'no'):
        name = input("Enter the name of the employee: ")
        salary = input("Enter the salary of that employee: ")
        if(name == 'no'):
            break
        dict_emp[name] = salary
    
Store()
print(dict_emp)

