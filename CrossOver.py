class Crossover:

    def __init__(self, _parent1, _parent2):
        self.Next_gen = [_parent1] + [_parent2]

    def single_point(self, ptr, ptr1, point):
        self.Next_gen.append(ptr[:point] + ptr1[point:])
        self.Next_gen.append(ptr1[:point] + ptr[point:])

    def two_point_crossover(self, ptr, ptr1, point1, point2):
        self.Next_gen.append(ptr[:point1]+ptr1[point1:point2]+ptr[point2:])
        self.Next_gen.append(ptr1[:point1] + ptr[point1:point2] + ptr1[point2:])

    def uniform_crossover(self, ptr, ptr1):
        self.Next_gen.append(ptr[:2] + ptr1[2:4] + ptr[4:6] + ptr1[6:8] + ptr[8:])
        self.Next_gen.append(ptr1[:2] + ptr[2:4] + ptr1[4:6] + ptr[6:8] + ptr1[8:])

    def GeneratePopulation(self):
            #for j in range(0, 3):
                j=0
                self.single_point(self.Next_gen[j], self.Next_gen[j+1], 5)
                self.two_point_crossover(self.Next_gen[j], self.Next_gen[j+1], 3, 6)
                self.uniform_crossover(self.Next_gen[j], self.Next_gen[j+1])
