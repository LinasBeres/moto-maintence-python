from motomaintence.util import load_motorcycle_maintenance

def load_morotcycle(motorcycleMake: str, motorcycleType: str):
    motorcycleMaintenance = load_motorcycle_maintenance(motorcycleMake, motorcycleType)
    return Motorcycle(motorcycleMaintenance)


class Motorcycle():
    def __init__(self, motorcycle_maintenance: dict):
        self.maintenance_info = motorcycle_maintenance

    def motorcycle_exists():
        return len(self.maintenance_info) != 0

    def get_item(self, item: str):
        pass

    def get_next_maintenance(self, km=-1, miles=-1):
        pass

    def get_torque_value(self, item: str):
        pass
