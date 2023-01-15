
class OBJECTIFS():
   #[T1, T2, T3, T4, T5]
   # [0,1,0,2,1,0]
    def assign_task_to_node(self, chromosome, task_list, node_list):
        for i in range(len(chromosome)):
            task_list[i].num_cpu = chromosome[i]
            for node in node_list:
                if node.num_cpu == chromosome[i]:
                    task_list[i].exec_task_time_required = task_list[i].task_exec_time(node.cpu_rate)
                    node.task_list.append(task_list[i])
        return (task_list, node_list)


    def fuction_objectifs_time_cost(self,chromosome, list_of_tasks, list_of_nodes):
        task_list, node_list = self.assign_task_to_node(chromosome, list_of_tasks, list_of_nodes)
        execTime = []
        chromosome_exec_cost = 0
        for noeud in node_list:
           execTime.append(noeud.node_execute_time()) 
        chromosome_exec_time = max(execTime)
        for task in task_list:
            for node in node_list:
                if task.num_cpu == node.num_cpu:
                    chromosome_exec_cost += task.task_cost(node.cpu_Time_cost, node.cpu_Memory_cost, node.cpu_Bandwidth_cost)
                    
        return (chromosome_exec_time, chromosome_exec_cost)
