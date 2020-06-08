import traceback


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyIterator:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter is None:
            self.counter += 1
            return
        else:
            raise StopIteration


class Vector(object):

    def __init__(self, obj):
        self.vector = obj

    def __add__(self, second_vector):
        try:
            for i in range(len(self.vector)):
                self.vector[i] += second_vector.vector[i]
        except IndexError:
            self.vector = None
        return self.vector

    def __sub__(self, second_vector):
        try:
            for i in range(len(self.vector)):
                self.vector[i] -= second_vector.vector[i]
        except IndexError:
            self.vector = None
        return self.vector

    def __str__(self):
        string = ""
        for elem in self.vector:
            string += str(elem) + ','
        return string[:len(string) - 1]

    def __mul__(self, second_vector):
        if len(self.vector) != len(second_vector):
            raise MyError("first vector!= second vector")
        mul = 0
        for i in range(len(self.vector)):
            mul += self.vector[i] * second_vector.vector[i]
        return mul

    def __const_mul__(self, const):
        self.vector = list(a * const for a in self.vector)
        return self.vector

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        arr = list(self.vector)
        return arr[index]

    def __eq__(self, second_vector):
        if self.vector == second_vector:
            return True
        if self.vector != second_vector:
            return False


a = [1, 2, 3]
v = Vector(a)
a.append(4)
v1 = Vector(a)
print(v == v1)
