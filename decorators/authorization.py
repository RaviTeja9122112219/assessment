def authorize(func):
    def wrapper(*args, **kwargs):
        # Check if user is authorized
        user = kwargs.get("user", "guest")
        if user == "admin":
            return func(*args, **kwargs)
        else:
            return "Unauthorized access."
    return wrapper

@authorize
def access_resource(resource, user="guest"):
    return f"Accessing resource: {resource}"

# Try to access a resource as an admin
print(access_resource("secret", user="admin"))

# Try to access a resource as a guest
print(access_resource("secret"))
