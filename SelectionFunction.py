import random


class Selection:

    def __init__(self, list_of_fitness, list_of_binary):
        self.strings = list_of_binary
        self.fitness = list_of_fitness

    def Roulett_Wheel_Selection(self):

            _sum, total, selected = 0, 0, []
            for j in range(len(self.fitness)):
                _sum += self.fitness[j][0]
            for i in range(0, 2):
                num = random.randint(0, _sum)
                for j in range(0, len(self.fitness)):
                    total += self.fitness[j][0]
                    if total >= num:
                        selected.append(self.strings[j])
                        break
            return selected

