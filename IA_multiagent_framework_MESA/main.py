from model import Model
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from random import randint
import random

def generer_initial_pos(num_agent, grid_size):
    liste_pos  = []
    for i in range(num_agent):
        pos = (randint(0,grid_size) , randint(0,grid_size))
        while (pos in liste_pos):
            pos = (randint(0,grid_size) , randint(0,grid_size))
        liste_pos.append(pos)
    return liste_pos

def generer_final_pos(num_agent, grid_size, liste_initial_pos):
    liste_pos  = []
    for i in range(num_agent):
        pos = (randint(0,grid_size) , randint(0,grid_size))
        while (pos in liste_pos or pos == liste_initial_pos[i]):
            pos = (randint(0,grid_size) , randint(0,grid_size))
        liste_pos.append(pos)
    return liste_pos

def agent_portrayal(agent):
    n = agent.model.num_agents
    for i in range(n): 
      if agent.unique_id == i:
          portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "text":agent.unique_id,
                 "text_color":"black",
                 "Layer": 0,
                 "Color": color[i],
                 "r": 0.5}
    return portrayal

if __name__ == '__main__':

    N = 30
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for  k in range(N) ]
    grid_size = 15
    initial_pos = generer_initial_pos(N, grid_size-1)
    final_pos = generer_final_pos(N,grid_size-1, initial_pos)
    grid = CanvasGrid(agent_portrayal, grid_size, grid_size, 700, 700)
    server = ModularServer(Model,
                        [grid],
                        "Money Model",
                        {"initial_pos_list" : initial_pos, "final_pos_list" : final_pos,"N":N, "grid_size":grid_size})
    print(initial_pos)
    print(final_pos)
    server.launch()

    
