from unittest import TestCase
from project.vehicle import Vehicle

DEFAULT_FUEL_CONSUMPTION = 1.25


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(fuel=56, horse_power=131)

    def test_init(self):
        self.assertEqual(56, self.car.capacity)
        self.assertEqual(131, self.car.horse_power)
        self.assertEqual(DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_normal_drive(self):
        km = 10
        fuel_needed = 12.5
        result = 43.5
        self.car.drive(km)
        self.assertEqual(result, self.car.fuel)

    def test_drive_with_low_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
            self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.car.refuel(0)
        expected_result = 56
        self.assertEqual(expected_result, self.car.fuel)

    def test_can_not_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(5)
            self.assertEqual("Too much fuel", str(ex.exception))

    def test__str__(self):
        result = "The vehicle has 131 horse power with 56 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, self.car.__str__())


