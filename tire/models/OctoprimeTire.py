from ..Tire import Tire

class OctoprimeTire(Tire):

  service_threshold = 3
  
  def __init__(self, wear_sensors):
    self.wear_sensors = wear_sensors

  def needs_service(self):
    sum = 0
    for num in self.wear_sensors:
      sum += num
      
    if sum >= self.service_threshold:
      return True
    else:
      return False