import unittest
from datetime import datetime

from tire.models.CarriganTire import CarriganTire
from tire.models.OctoprimeTire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
  def test_needs_service(self):
    wear_sensors = [0, 0.2, 1, 0.4]

    tire = CarriganTire(wear_sensors)
    self.assertTrue(tire.needs_service())

  def test_needs_service_equal(self):
    wear_sensors = [0, 0.2, 0.9, 0.4]

    tire = CarriganTire(wear_sensors)
    self.assertTrue(tire.needs_service())

  def test_no_service(self):
    wear_sensors = [0, 0.2, 0.6, 0.3]

    tire = CarriganTire(wear_sensors)
    self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
  def test_needs_service(self):
    wear_sensors = [1, 1, 1, 1]

    tire = OctoprimeTire(wear_sensors)
    self.assertTrue(tire.needs_service())

  def test_needs_service_equal(self):
    wear_sensors = [0.75, 0.75, 0.75, 0.75]

    tire = OctoprimeTire(wear_sensors)
    self.assertTrue(tire.needs_service())

  def test_no_service(self):
    wear_sensors = [0, 0.2, 0.6, 0.4]

    tire = OctoprimeTire(wear_sensors)
    self.assertFalse(tire.needs_service())        
    