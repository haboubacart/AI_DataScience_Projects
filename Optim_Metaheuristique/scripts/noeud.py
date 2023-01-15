
class NOEUD():

    def __init__(self, cpu_rate, num_cpu, cpu_Time_cost, cpu_Memory_cost, cpu_Bandwidth_cost):
        self.task_list = []
        self.cpu_rate = cpu_rate
        self.num_cpu = num_cpu
        self.cpu_Time_cost = cpu_Time_cost
        self.cpu_Memory_cost = cpu_Memory_cost
        self.cpu_Bandwidth_cost = cpu_Bandwidth_cost

    def node_execute_time(self):
        time = 0
        for task in self.task_list:
            time += task.length / self.cpu_rate
        return time
        
       
        