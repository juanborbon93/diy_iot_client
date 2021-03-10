import numpy as np
from random import randint,random



class Feed:
    def __init__(self):
        self.time_step = 0
        self.p1 = randint(15,30)
        self.p2 = randint(15,30)
        self.phi = random()

    def get_value(self):
        value =  np.sin(np.pi*self.time_step/self.p1)+np.sin(self.phi+np.pi*self.time_step/self.p2)
        self.time_step += 1
        return value