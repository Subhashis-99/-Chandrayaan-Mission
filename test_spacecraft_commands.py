
import unittest
from spacecraft import Spacecraft


class TestSpacecraftCommands(unittest.TestCase):

# Test case to verify that moving forward updates the spacecraft's position correctly

    def test_move_forward(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.move_forward()
        self.assertEqual(spacecraft.position, [0, 1, 0])

 # Test case to verify that moving backward updates the spacecraft's position correctly

    def test_move_backward(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.move_backward()
        self.assertEqual(spacecraft.position, [0, -1, 0])

 # Test case to verify that turning left updates the spacecraft's position correctly

    def test_turn_left(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_left()
        self.assertEqual(spacecraft.direction, 'W')

 # Test case to verify that turning right updates the spacecraft's position correctly

    def test_turn_right(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_right()
        self.assertEqual(spacecraft.direction, 'E')

 # Test case to verify that turning upward updates the spacecraft's position correctly

    def test_turn_up(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, 'Up')

 # Test case to verify that turning downward updates the spacecraft's position correctly

    def test_turn_down(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_down()
        self.assertEqual(spacecraft.direction, 'Down')


if __name__ == '__main__':
    unittest.main()
