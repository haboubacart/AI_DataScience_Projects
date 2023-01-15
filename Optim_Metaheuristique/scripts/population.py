from re import I
from individual import INDIVIDUAL
from random import randint, shuffle, random
from copy import copy

class POPULATION():

    def __init__(self, population_size, number_task, number_fogNode, number_CloudNode):
        self.population_size = population_size
        self.number_task = number_task
        self.number_fogNode = number_fogNode
        self.number_cloudNode = number_CloudNode
        self.population = []


    def initialize_population(self, tasks, noeuds):
        number_Node = self.number_fogNode + self.number_cloudNode -1
        for i in range(self.population_size):
            individu = INDIVIDUAL()
            for j in range(self.number_task):
                gene = randint(0,number_Node)
                individu.chromosome.append(gene)
            individu.evaluate(tasks, noeuds)
            self.population.append(individu)
   
    def next_generation(self, tasks, noeuds, mutation_probability):

        shuffle(self.population)

        time_gen  = self.population[:int(len(self.population)/2)]
        cost_gen = self.population[int(len(self.population)/2):]

        time_gen  = self.select_phenotypes(time_gen, 'time')
        cost_gen = self.select_phenotypes(cost_gen, 'cost')

        alpha = random()            
        if alpha <= 0.4:
            time_gen  = self.crossover(time_gen)
            cost_gen = self.crossover(cost_gen)
        
        time_gen  = self.mutate(time_gen, mutation_probability)
        cost_gen = self.mutate(cost_gen, mutation_probability)

        

        next_generation = time_gen + cost_gen

        # Evaluate creatures
        for individu in next_generation:
            individu.evaluate(tasks, noeuds)
        self.population =  next_generation

    def select_phenotypes(self, population, type):
        """
        Rank based selection (Stochastic universal sampling)
        """
        # list, sorted by rank and filtered by constraint
        if type == 'time':
            sorted_population = sorted( population,
                                        key=lambda individu: individu.time,
                                        reverse=True )
        else:
            sorted_population = sorted( population,
                                        key=lambda individu: individu.cost,
                                        reverse=True )        

        # List with boundaries of interval for rank probability

        sorted_population = sorted_population [:int(len(population)*0.9)]
        return sorted_population
    
    def get_probability_interval(self, max_rank):
        """
        Create list with probability of ranks, interval
        of rank 1 is first in list
        """ 
        sum_ranks = max_rank*(max_rank+1)/2
        interval = [float(max_rank)/sum_ranks]
        for rank in range(max_rank-1,0,-1):
            interval.append( interval[-1] + float(rank)/sum_ranks )

        return interval
    
    def mutate(self, sub_population,  mutation_probability):
        new_pop = []
        for individu in sub_population:
            alpha = random()            
            if alpha <= mutation_probability:
                individu = self.mutate_individual(individu)   
            new_pop.append(individu)
        return new_pop

    #[2, 1, 5, 3, 4]
    def mutate_individual(self, individu):
        index = randint(0, len(individu.chromosome) - 1)
        gene = randint (0, self.number_fogNode + self.number_cloudNode -1)
        individu.chromosome[index] = gene
        return individu
 
    def crossover(self, population, breeder_size=4):
        """
        Chose n creatures and mate those, two parents
        giving birth to two offsprings. Offsprings will
        replace their parents.
        """
        offsprings = []
        shuffle(population)
        for _ in range(int(breeder_size/2)):
            # Genotype of mother and father will be
            # replaced with genotype of offsprings
            mother = population.pop()
            father = population.pop()

            children_chromosomes = self.single_point_recombine(mother, father)

            mother.chromosome = children_chromosomes[0]
            father.chromosome = children_chromosomes[1]

            offsprings.append(mother)
            offsprings.append(father)
        population += offsprings
        new_pop = population
        return new_pop

    def single_point_recombine(self, individu1, individu2):
        cross_point = randint(0, len(individu1.chromosome) - 1)
        new_ind1_chromosome = individu1.chromosome[:cross_point] + individu2.chromosome[cross_point:]
        new_ind2_chromosome = individu1.chromosome[cross_point:] + individu2.chromosome[:cross_point]
        return [new_ind1_chromosome, new_ind2_chromosome]

    def shows(self, popu):
        for elm in popu:
            print(elm.chromosome)
        print(' ')


    def max_population_time(self, population):
        p_time = []
        for individu in population:
            p_time.append(individu.time)
        return max(p_time)

    def max_population_cost(self, population):
        p_cost = []
        for individu in population:
            p_cost.append(individu.cost)
        return max(p_cost)





     