from ..Engine import Engine

class CapuletEngine(Engine):

    mileage_threshold = 30000

    def __init__(self, current_mileage, last_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > self.mileage_threshold:
            return True
        else:
            return False