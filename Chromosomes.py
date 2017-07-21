
class Chromosome:

    def __init__(self, fit_list, pop_size):
        self.hash = {}
        self.fitness_list = fit_list
        self.number = pop_size

    def show_hash(self):
        for k, v in self.hash.items():
            print("{0}:{1} ".format(k, v), end=" ")
        print("\n")

    def check_for_population(self):  # Check if 90% of population has same Fitness value or not

        for x in self.fitness_list:

            if x[0] not in self.hash:
                self.hash[x[0]] = 1
            else:
                self.hash[x[0]] += 1

        _max = -999999999999999
        for x in self.hash:
            if self.hash[x] > _max:
                _max = self.hash[x]
        self.show_hash()
        if _max >= int(0.9 * self.number):
            return True
        else:
            return False



