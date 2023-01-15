from task import TASK
from noeud import NOEUD
from objectifs import OBJECTIFS
import random 

def generer_task(N, length_interval = [0,100], memory_interval = [50,200], bandwidth_interval = [50,200]):
    list_task = []
    for i in range(N):
        length = random.randint(length_interval[0],length_interval[1])
        memory_required = random.randint(memory_interval[0],memory_interval[1])
        bandwidth_required = random.randint(bandwidth_interval[0],bandwidth_interval[1])
        task = TASK(length, memory_required, bandwidth_required)
        list_task.append(task)
    return list_task


def generate_fogs(N, cpu_rate_interval = [500, 2000], cpu_usage_cost_interval = [0.2, 0.5], memory_usage_cost_interval = [0.01, 0.03], bandwidth_usage_cost_interval = [0.01, 0.02]):
    list_noeuds = []
    liste_num_cpu = []
    for i in range(N):
        num_cpu = i
        liste_num_cpu.append(num_cpu)
        cpu_rate = random.randint(cpu_rate_interval[0], cpu_rate_interval[1])
        cpu_Time_cost = random.uniform(cpu_usage_cost_interval[0], cpu_usage_cost_interval[1])
        cpu_Memory_cost = random.uniform(memory_usage_cost_interval[0], memory_usage_cost_interval[1])
        cpu_Bandwidth_cost = random.uniform(bandwidth_usage_cost_interval[0], bandwidth_usage_cost_interval[1])

        noeud_fog = NOEUD(cpu_rate, num_cpu, cpu_Time_cost, cpu_Memory_cost, cpu_Bandwidth_cost)
        list_noeuds.append(noeud_fog)
    return list_noeuds



def generate_clouds(N, cpu_rate_interval = [3000, 10000], cpu_usage_cost_interval = [1.0, 2.1], memory_usage_cost_interval = [0.02, 0.05], bandwidth_usage_cost_interval = [0.05, 0.01]):
    list_noeuds = []
    liste_num_cpu = []
    for i in range(N):
        num_cpu = i
        liste_num_cpu.append(num_cpu)
        cpu_rate = random.randint(cpu_rate_interval[0],cpu_rate_interval[1])
        cpu_Time_cost = random.uniform(cpu_usage_cost_interval[0],cpu_usage_cost_interval[1])
        cpu_Memory_cost = random.uniform(memory_usage_cost_interval[0],memory_usage_cost_interval[1])
        cpu_Bandwidth_cost = random.uniform(bandwidth_usage_cost_interval[0],bandwidth_usage_cost_interval[1])

        noeud_fog = NOEUD(cpu_rate, num_cpu, cpu_Time_cost, cpu_Memory_cost, cpu_Bandwidth_cost)
        list_noeuds.append(noeud_fog)
    
    return list_noeuds

def generate_sytem_noeuds(N_fog, N_cloud):
    fog_nod_list = generate_fogs(N_fog)
    cloud_node_list = generate_clouds(N_cloud)
    node_list = []
    for node in cloud_node_list:
        node.num_cpu = node.num_cpu + len(fog_nod_list) 
    node_list = fog_nod_list + cloud_node_list
    return node_list


# temps d'xecution des taches a revoir 
# contrainte à prendre en compte
# utilisation d'energie à prendre en compte parmis les objectifs à minimser 

"""if __name__ == '__main__':
    tasks = generer_task(12)
    noeuds = generate_sytem_noeuds(3,2)
    chromosome1 = [0,1,0,2,1,0,0,2,3,4,2,4]
    chromosome2 = [0,1,0,3,1,4,0,2,3,4,2,4]
    chromosome3 = [1,1,0,2,1,2,0,2,1,4,2,4]
    obj = OBJECTIFS()
    res_eval1 = obj.fuction_objectifs_time_cost(chromosome1, tasks, noeuds)
    res_eval2 = obj.fuction_objectifs_time_cost(chromosome2, tasks, noeuds)
    res_eval3 = obj.fuction_objectifs_time_cost(chromosome3, tasks, noeuds)
    print(res_eval1)
    print(res_eval2)
    print(res_eval3)"""

