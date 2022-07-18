import unittest
import time
from simple_pid import Controller


class ControllerTest(unittest.TestCase):
    def test_controller(self):
        test_ysp = 15
        plant_value = 100
        next_input = plant_value
        test_controller = Controller(1, 0.1, 0.01, test_ysp)

        steps = 100
        while steps > 0:
            next_input = test_controller.update(float(next_input))
            plant_value += next_input
            print(f'{next_input}, {plant_value}')
            
            steps -= 1
            time.sleep(1)


if __name__ == "__main__":
    unittest.main(verbosity=3)


        