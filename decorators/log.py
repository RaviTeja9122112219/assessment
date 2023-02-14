def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"{func.__name__} returns the value {result}")
        
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b


result = add(3, 4)
