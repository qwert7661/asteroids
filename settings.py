from constants import *

class Difficulty():
    def __init__(self, ASTEROID_KINDS, ASTEROID_SPAWN_RATE):
        self.asteroid_kinds = ASTEROID_KINDS
        self.asteroid_spawn_rate = ASTEROID_SPAWN_RATE
    def scale(self,dt):
        self.asteroid_kinds 

        self.asteroid_spawn_rate += (ASTEROID_SPAWN_RATE_FACTOR * dt)