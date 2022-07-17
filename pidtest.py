import unittest

from simple_pid import Controller


class ControllerTest(unittest.TestCase):
    def test_controller(self):
        test_ysp = 15
        test_initial = 100
        next_input = test_initial
        test_controller = Controller(1, 0.1, 0.01, test_ysp)

        while True:
            next_input = test_controller.update(float(next_input))
            print(next_input)
            break


if __name__ == "__main__":
    unittest.main(verbosity=3)


        