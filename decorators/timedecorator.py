import time

def time_check(func):

    def inner():

        st = time.time()

        func()

        end = time.time()

        ex_time = st - end

        print(ex_time)

    return inner

@time_check

def hello():

    time.sleep(2)

    return "hello world"



hello()