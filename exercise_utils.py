class fiberator:
    def __init__(self):
        self.i, self.j = 0, 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n == 1:
            return self.i
        if self.n > 2:
            self.i, self.j = self.j, self.i + self.j
        return self.j
