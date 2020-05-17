from datetime import datetime as dt

def duration(func):
    def wrapped(*args, **kwargs):
        start = dt.now()
        res = func(*args)
        print(f"time taken in microseconds by {func.__name__} ", (dt.now()-start).microseconds)
        return res
    return wrapped