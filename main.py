class Line:
    def __init__(self, *args):
        self.items = list(args)
    def __str__(self):
        return f'{self.items[:-1]} | {self.items[-1]}'

class Matrix:
    def __init__(self, *args):
        self.lines = list(*args)
    def solve(self):
        for i in range(len(self.lines)):
            coeff = self.lines[i].items[i] * 1
            for j in range(len(self.lines[i].items)):
                self.lines[i].items[j] /= coeff

            for j in range(i + 1, len(self.lines)):
                coeff = self.lines[j].items[i] / self.lines[i].items[i]
                for k in range(i, len(self.lines[j].items)):
                    self.lines[j].items[k] -= coeff * self.lines[i].items[k]

    def result(self):
        



m = Matrix((Line(2, 5, 4, 1, 20), Line(1, 3, 2, 1, 4), Line(2, 10, 9, 7, 40), Line(3, 8, 9, 2, 37)))
m.solve()
print(*m.lines, sep='\n')
