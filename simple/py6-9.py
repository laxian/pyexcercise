class Fib(object):
    def __str__(self):
        return str(self.l)

    def __call__(self, num):
        a, b, l = 0, 1, []
        for i in range(0, num):
            l.append(a)
            a, b = b, a + b
        return str(l)


f = Fib()
print(f(10))
