import time

current_time = time.time()
print(f"{current_time} seconds since Jan 1st, 1970")




def code_timer(function):
    def wrapper_function():
        time_x = time.time()
        function()
        time_y = time.time()
        duration_z = time_y - time_x
        print(f"{function.__name__} run speed: {duration_z}")

    return wrapper_function


@code_timer
def fast_function():
    for i in range(1000000):
        i * i


@code_timer
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
