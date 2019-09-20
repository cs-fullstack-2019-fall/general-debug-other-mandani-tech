from unittest import TestCase
from Car import Car

class TestCar(TestCase):
    def setUp(self):
        self.car = Car()

    def test_average_speed(self):
        self.fail()

    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)
