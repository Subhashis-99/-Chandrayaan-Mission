
class Spacecraft:

    def __init__(
        self,
        x,
        y,
        z,
        direction,
        ):

         # Initialize the spacecraft's position and direction

        self.position = [x, y, z]
        self.direction = direction

    def move_forward(self):

        # Move the spacecraft forward based on its current direction

        if self.direction == 'N':
            self.position[1] += 1
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'E':
            self.position[0] += 1
        elif self.direction == 'W':
            self.position[0] -= 1
        elif self.direction == 'Up':
            self.position[2] += 1
        elif self.direction == 'Down':
            self.position[2] -= 1

    def move_backward(self):

         # Move the spacecraft backward based on its current direction

        if self.direction == 'N':
            self.position[1] -= 1
        elif self.direction == 'S':
            self.position[1] += 1
        elif self.direction == 'E':
            self.position[0] -= 1
        elif self.direction == 'W':
            self.position[0] += 1
        elif self.direction == 'Up':
            self.position[2] -= 1
        elif self.direction == 'Down':
            self.position[2] += 1

    def turn_left(self):

        # Turn the spacecraft 90 degrees to the left

        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):

         # Turn the spacecraft 90 degrees to the right

        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):

        # Turn the spacecraft upwards

        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'E' or self.direction == 'W':

            # Handle turning up from horizontal directions

            self.direction = 'Up'

    def turn_down(self):

        # Turn the spacecraft downwards

        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'E' or self.direction == 'W':

            # Handle turning down from horizontal directions

            self.direction = 'Down'


if __name__ == '__main__':
    commands = ['f', 'r', 'u', 'b', 'l']
    starting_position = [0, 0, 0]
    initial_direction = 'N'

    spacecraft = Spacecraft(starting_position[0], starting_position[1],
                            starting_position[2], initial_direction)

     # Execute the list of commands

    for command in commands:
        if command == 'f':
            spacecraft.move_forward()
        elif command == 'b':
            spacecraft.move_backward()
        elif command == 'l':
            spacecraft.turn_left()
        elif command == 'r':
            spacecraft.turn_right()
        elif command == 'u':
            spacecraft.turn_up()
        elif command == 'd':
            spacecraft.turn_down()

    # Display the final position and direction of the spacecraft

    final_position = tuple(spacecraft.position)
    final_direction = spacecraft.direction

    print ('Final Position:', final_position)
    print ('Final Direction:', final_direction)
