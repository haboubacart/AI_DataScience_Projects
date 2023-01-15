import utils
from population import POPULATION
import matplotlib.pyplot as plt


if __name__ == '__main__':
    NB_TASKS = 100
    NB_FOG = 10
    NB_CLOUD = 5    
    POP_SIZE = 400
    NUMBER_GENERATIONS   = 10
    MUTATION_PROBABILITY = 0.02

    TASKS = utils.generer_task(NB_TASKS)
    NOEUDS = utils.generate_sytem_noeuds(NB_FOG,NB_CLOUD)
    POP = POPULATION(POP_SIZE, NB_TASKS, NB_FOG, NB_CLOUD)
    POP.initialize_population(TASKS, NOEUDS)

    """print("\n===========   Starting  ===============")
    for i in range(NUMBER_GENERATIONS):
        POP.next_generation(TASKS, NOEUDS, MUTATION_PROBABILITY)
        print("generation number : ", i)"""

    time_obj = [(individu.time / POP.max_population_time(POP.population) )  for individu in POP.population]
    cost_obj = [(individu.cost / POP.max_population_cost(POP.population) )  for individu in POP.population]

    plt.scatter(time_obj, cost_obj)
    plt.xlabel('Makespan')
    plt.ylabel('Cost')
    plt.title('makespan en fonction de cout')
    plt.show()