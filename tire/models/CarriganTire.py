from ..Tire import Tire

class CarriganTire(Tire):

  service_threshold = 0.9
  
  def __init__(self, wear_sensors):
    self.wear_sensors = wear_sensors

  def needs_service(self):
    
    wear_check = False

    for num in self.wear_sensors:
      if num >= self.service_threshold:
        wear_check = True
        break
      
    return wear_check