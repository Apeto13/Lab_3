def repetitions(func):
    def decorator():
        x = int(input("Enter a number of repetitions: "))
        for _ in range(x):
            func()
    return decorator


@repetitions
def hello():
    print("Hello")

hello()