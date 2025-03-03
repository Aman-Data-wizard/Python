def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper  # Return the wrapper function

@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
