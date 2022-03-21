from decimal import Decimal
from fractions import Fraction as frac
class Line:
    def __init__(self, *args):
        self.items = list(args)

    def frame(n):
        return str(n)

    def end(self):
        return self.items[-1]

    def __str__(self):
        return ' '.join(Line.frame(i) for i in self.items[:-1])

    def __len__(self):
        return len(self.items)

    def __getitem__(self, ind):
        return self.items[ind]
    def __setitem__(self, ind, key):
        self.items[ind] = key
    def __mul__(self, other: int):
        items = [0] * len(self)
        for i in range(len(self)):
            items[i] = self.items[i] * other
        return Line(*items)
    def __sub__(self, other):
        items = [0] * len(self)
        for i in range(len(self)):
            items[i] = self.items[i] - other.items[i]
        return Line(*items)
    def __div__(self, other: int):
        items = [0] * len(self)
        for i in range(len(self)):
            items[i] = self.items[i] / other
        return Line(*items)
    __floordiv__ = __div__
    def __add__(self, other):
        items = [0] * len(self)
        for i in range(len(self)):
            items[i] = self.items[i] + other.items[i]
        return Line(*items)


class Matrix:
    def __init__(self, *args):
        self.lines = list(*args)
        self.startlines = self.lines.copy()

    def __getitem__(self, ind):
        return self.lines[ind]

    def __setitem__(self, ind, key):
        self.lines[ind] = key

    def __str__(self):
        def calculate_max(lines): return len(max(lines, key=len)) + 1
        retreat = calculate_max(map(str, self.lines))
        return '\n'.join(str(i) + ' ' * (retreat - len(str(i))) + f"| {i.end()}" for i in self.lines)
    __repr__ = __str__
    def __len__(self):
        return len(self.lines)

    def solve(self, out=False):
        if out:
            print(self, end='\n\n')
        for i in range(len(self)):
            if out:
                print(self, end='\n\n')
            ratio = self[i][i]
            for j in range(len(self[i])):
                self[i][j] = frac(str(self[i][j])) / frac(str(ratio))
            for j in range(i + 1, len(self)):
                ratio = frac(str(self[j][i])) / frac(str(self[i][i]))
                for k in range(i, len(self[j])):
                    self[j][k] -= ratio * self[i][k]
        if out:
            print(self, end='\n\n')

    def result(self):
        n, m = len(self), len(self[0])
        ans = [0 for _ in range(m - 1)]
        for i in range(n - 1, -1, -1):
            foo = 0
            for j in range(i + 1, m - 1):
                foo += self[i][j] * ans[j]
            ans[i] = self[i][-1] - foo
        return ans

    def check(self, results):
        for line in self.startlines:
            res = sum(results[el] * line[el] for el in range(len(line) - 1))
            if res != line[-1]:
                return False
        return True

if __name__ == '__main__':
    m = Matrix((Line(2,5,4,1,20),Line(1,3,2,1,4),Line(2,10,9,7,40),Line(3,8,9,2,37)))
    m.solve(out=True)
    print(f"Result: {list(map(str, m.result()))}")
