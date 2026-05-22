# x = 10  # Global variable

# def my_func():
#     x = 5  # Local variable
#     print(x)  # Output: 5

# my_func()
# print(x)  # Output: 10 (global x remains unchanged)


x = 10  # Global variable

def modify_global():
    global x
    x = 5  # Modifies the global x

modify_global()
print(x)  # Output: 5