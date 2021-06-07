import functools

def start_end_decorator(funct):

    @functools.wraps(funct)
    def wrapper(*args, **kwargs):
        #Do..
        result=funct(*args, **kwargs)
        #Do..
        return result
    return wrapper

@start_end_decorator
def __init__(x):
    return x+5

#print_name=start_end_decorator(__init__)
