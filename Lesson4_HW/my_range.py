class MyRange:

    def __iter__(self):
        return self

    def __init__(self, *args):
        self.start = -1
        self.step = 1
        if len(args) == 1:
            self.end = args[0]
        elif len(args) == 2:
            self.start = args[0]-1
            self.end = args[1]
        elif len(args) == 3:
            if args[2] == 0:
                raise ValueError('MyRange() arg 3 must not be zero')
            self.start = args[0]-args[2]
            self.end = args[1]
            self.step = args[2]

    def __next__(self):
        self.start += self.step
        if self.step > 0:
            if self.start < self.end:
                return self.start
            else:
                raise StopIteration
        elif self.step < 0:
            if self.start > self.end:
                return self.start
            else:
                raise StopIteration

