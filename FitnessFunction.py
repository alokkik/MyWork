
class Fitness:

    def __init__(self, _var, _var2, size):
        self.total_size = size
        self.fit_list = []
        self.items_list = _var
        self.binary_strings = _var2

    def Calculate_fitness(self):

        for string in self.binary_strings:
                value_sum, size_sum = 0, 0
                for j in range(0, len(string)):
                    if string[j] is 1:
                        value_sum += self.items_list[j][0]
                        size_sum += self.items_list[j][1]

                while size_sum > self.total_size:
                    for j in range(0, len(string), 1):
                        if string[j] is 1:
                            string[j] = 0
                            value_sum -= self.items_list[j][0]
                            size_sum -= self.items_list[j][1]
                            break

                self.fit_list.append([value_sum, size_sum])

        return self.fit_list

    def show_fitness(self):
        for x in self.fit_list:
            print(x)

