from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
import numpy as np
from astar import ASTAR

astar = ASTAR()
 
class Model(Model):
    """Implémentation.
    """

    def __init__(self, initial_pos_list, final_pos_list, N, grid_size):
        self.num_agents = N
        self.grid_size = grid_size
        self.grid = SingleGrid(grid_size, grid_size, True)
        self.schedule = RandomActivation(self)
        self.initial_pos_list = initial_pos_list
        self.final_pos_list = final_pos_list
        self.running = True

        # Create agents
        for i in range(self.num_agents):
            
            agent = Agent(i, self, initial_pos_list[i], final_pos_list[i])
            self.schedule.add(agent)
            # Add the agent to a random grid cell
            print((initial_pos_list[i][0], initial_pos_list[i][1]))
            self.grid.position_agent(agent)
            self.grid.move_agent(agent,(initial_pos_list[i][0], initial_pos_list[i][1]))
    

    def generate_binaire_grid(self):
        grid = np.zeros([self.grid_size, self.grid_size])
        for cell in self.grid.coord_iter():
            if(cell[0] != None):
                grid[cell[2]] [cell[1]] = 1
        return(grid)

    def step(self):
        self.schedule.step()
    
    def run_model(self, n):
            self.step()


class Agent(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model, initial_pos , final_pos):
        super().__init__(unique_id, model)
        self.initial_pos = initial_pos
        self.final_pos = final_pos

    #move!!!
    def move(self):

        grid = self.model.generate_binaire_grid()
        best_step = astar.astar(grid, self.pos, self.final_pos)

        if (best_step):
            new_pos = best_step[-1]
            try :
                self.model.grid.move_agent(self, new_pos)
            except:
                agent_blocant = self.model.grid.get_cell_list_contents([new_pos])[-1]
                if (agent_blocant.pos != agent_blocant.final_pos):
                    agent_blocant.move()
                else:
                    print('case occupée, je suis ', self.pos, 'bloque par ',agent_blocant.pos, 'je veux aller a ',new_pos)
                    possible_steps = agent_blocant.model.grid.get_neighborhood(agent_blocant.pos, moore = False, include_center=False) 
                    print ("agent bloc à ", agent_blocant.pos)
                    print("voisins de l'agent blocant ", possible_steps)

                    if (self.pos in possible_steps):
                        possible_steps.remove(self.pos)

                    for position in possible_steps:
                        if (abs(agent_blocant.pos[0] - position[0]) == self.model.grid_size-1):
                            possible_steps.remove(position)
                        if (abs(agent_blocant.pos[1] - position[1]) ==  self.model.grid_size-1):
                            possible_steps.remove(position)
                
                    print('deplacement possibles pour ag blocant ',possible_steps)
                    for position in possible_steps:
                        if agent_blocant.model.grid.is_cell_empty(position):
                            print('agent blocant se deplace vers', position)
                            agent_blocant.model.grid.move_agent(agent_blocant, position)
                            break

                    if self.model.grid.is_cell_empty(new_pos):
                        self.model.grid.move_agent(self,new_pos)


        else:
            print("arrivé!!")
            print(self.pos == self.final_pos)
        

    def step(self):
        self.move()
        