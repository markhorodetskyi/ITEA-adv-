from time import time, sleep


def benchmark(method, critical_time):
    def helper(*args, **kwargs):
        time_start = time()
        res = method(*args, **kwargs)
        print(f'Time process: {time() - time_start} sec.')
        print(f'WARNING! Execution time is longer than {critical_time}') \
            if time() - time_start > critical_time \
            else print('', end='')
        return res

    return helper


class DecorTimeCrit:
    def __init__(self, critical_time):
        self.critical_time = critical_time

    def __call__(self, cls):
        def helper(*args, **kwargs):
            for attr in dir(cls):
                if attr.startswith('__'):
                    continue

                new_attr = getattr(cls, attr)

                if callable(new_attr):
                    decor_method = benchmark(new_attr, self.critical_time)
                    setattr(cls, attr, decor_method)

            return cls(*args, **kwargs)

        return helper


@DecorTimeCrit(critical_time=0.45)
class Test:

    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


t = Test()

t.method_1()
t.method_2()
