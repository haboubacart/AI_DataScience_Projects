
class TASK():

    def __init__(self, length, exec_task_memory_required, exec_task_bandwidth_required) :
        self.length = length
        self.exec_task_memory_required = exec_task_memory_required
        self.exec_task_bandwidth_required = exec_task_bandwidth_required
        self.exec_task_time_required = -1
        self.num_cpu = -1

    def task_exec_time(self,cpu_rate):
        return (self.length/cpu_rate)

        #cpu_Time_cost_vector tableau contenant les couts d'utiisations des Neouds par unité de temps consommée
    def time_cost(self, cpu_Time_cost):
        return cpu_Time_cost * self.exec_task_time_required

    #cpu_Memory_cost_vector tableau contenant les couts d'utiisations des Neouds par unité de mémoire consommée
    def memory_cost(self, cpu_Memory_cost):
        return cpu_Memory_cost * self.exec_task_memory_required

    #cpu_use_cost tableau contenant les couts d'utiisations des Neouds par unité de temps de bande passante consommée
    def bandwidth_cost(self, cpu_Bandwidth_cost):
        return cpu_Bandwidth_cost * self.exec_task_bandwidth_required

    def task_cost(self, cpu_Time_cost, cpu_Memory_cost, cpu_Bandwidth_cost):
        return self.time_cost(cpu_Time_cost) + self.memory_cost(cpu_Memory_cost) #+ self.bandwidth_cost(cpu_Bandwidth_cost) 
