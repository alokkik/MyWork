import random


class Mutate:


    def mutate_strings(self, New_gen):

        for string in New_gen:

            j = random.randint(0, len(string)-1)

            if string[j] is 1:
                string[j] = 0
            else:
                string[j] = 1
        return New_gen