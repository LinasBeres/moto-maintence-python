from pyMotoMaintence.util import loadMotorcycleMaintence

def loadMorotcycle(motorcycleMake: str, motorcycleType: str):
    motorcycleMaintence = loadMotorcycleMaintence(motorcycleMake, motorcycleType)
    return Motorcycle(motorcycleMaintence)


class Motorcycle():
    def __init__(self, motorcycleMaintence: dict):
        self.maintenceInfo = motorcycleMaintence

    def exists():
        return len(self.maintenceInfo) != 0
