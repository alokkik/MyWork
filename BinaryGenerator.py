import random


class Generator:
    def __init__(self):
        self.New_gen = []

    def decimal_to_binary(self, var):
        ptr = []
        while var != 0:
            ptr = ptr+[var % 2]
            var = var//2
            ptr = ptr[::-1]

        while len(ptr) is not 10:
            ptr = [0] + ptr
        return ptr

    def binary_string_generator(self):
        for i in range(0, 7):
            num = random.randint(0, 1023)
            self.New_gen.append(self.decimal_to_binary(num))

    def show_new_gen(self):
        for i in self.New_gen:
            print(i)

