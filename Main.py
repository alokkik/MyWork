import FitnessFunction as Ff
import SelectionFunction as Sf
import Chromosomes as Ch
import CrossOver as Co
import BinaryGenerator as Bg
import Input
import Mutation


# Creating an Enter class object (_input) to get input from file

_input = Input.Enter()
_input.get_input()
# _input.items_list                                 list of items read from file grouped together as a tuple

# Creating an object of BinaryGenerator (_binary) class to generate Chromosomes(Binary Strings)

_binary = Bg.Generator()
_binary.binary_string_generator()
#  list of Chromosomes (Binary Strings)
i=0
# Creating an object of FitnessFunction class (_fit)
while True:
    _fit = Ff.Fitness(_input.items_list, _binary.New_gen, 11)

    _fit.Calculate_fitness()
    # _fit.fit_list                                     list of tuples having Fitness value and Volume coupled together

    # Creating an object of Chromosomes ( _chromosome )  to check the Population of chromosomes for termination

    _chromosome = Ch.Chromosome(_fit.fit_list, len(_fit.fit_list))

    if _chromosome.check_for_population() is True:
        print(" The Maximum profit we can achieve is {}".format(max(_chromosome.hash)))
        break

    # Creating an object of Selection class (_select) to Select two best Parent (_parent1, _parent2)

    _select = Sf.Selection(_fit.fit_list, _binary.New_gen)

    _parent = _select.Roulett_Wheel_Selection()

    # Creating an object of Crossover class (_cross)

    _cross = Co.Crossover(_parent[0], _parent[1])

    _cross.GeneratePopulation()

    _mut = Mutation.Mutate()

    _binary.New_gen = _mut.mutate_strings(_cross.Next_gen)

    # print(_binary.New_gen)

