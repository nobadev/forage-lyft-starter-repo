from ..Engine import Engine

class WilloughbyEngine(Engine):

    mileage_threshold = 60000

    def __init__(self, current_mileage, last_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self, mileage_threshold):
        if self.current_mileage - self.last_service_mileage > mileage_threshold:
            return True
        else:
            return False
