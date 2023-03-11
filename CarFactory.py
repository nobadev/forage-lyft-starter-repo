from engine.models.SternmanEngine import SternmanEngine
from engine.models.WilloughbyEngine import WilloughbyEngine
from engine.models.CapuletEngine import CapuletEngine

from battery.models.SpindlerBattery import SpindlerBattery
from battery.models.NubbinBattery import NubbinBattery

from car import Car

class CarFactory():
  def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)

  def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


  def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)


  def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = SternmanEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


  def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)
    
  