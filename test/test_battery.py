import unittest
from datetime import datetime

from battery.models.SpindlerBattery import SpindlerBattery
from battery.models.NubbinBattery import NubbinBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_no_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_no_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())