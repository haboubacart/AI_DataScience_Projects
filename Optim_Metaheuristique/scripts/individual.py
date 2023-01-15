from objectifs import OBJECTIFS

obj = OBJECTIFS()

class INDIVIDUAL():

    def __init__(self):
        self.chromosome = []
        self.time = -1
        self.cost = -1

    def evaluate(self, tasks, noeuds):
        (self.time , self.cost ) = obj.fuction_objectifs_time_cost (self.chromosome, tasks, noeuds)
        