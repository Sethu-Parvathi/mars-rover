class RobotSimulator:
    def __init__(self, grid_dimension, starting_position, obstacles):
        self.grid_dimension = grid_dimension
        self.current_position = starting_position
        self.obstacles = obstacles
        self.orientation = starting_position[2]
        self.directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        self.turn_right_map = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.turn_left_map = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}

    def _turn_right(self):
        self.orientation = self.turn_right_map[self.orientation]

    def _turn_left(self):
        self.orientation = self.turn_left_map[self.orientation]

    def _move(self):
        dx, dy = self.directions[self.orientation]
        x, y, _ = self.current_position
        new_x, new_y = x + dx, y + dy
        if not self._violation((new_x, new_y)):
            self.current_position = (new_x, new_y, self.orientation)

    def _violation(self, position):
        x, y = position
        if x < 0 or y < 0 or x >= self.grid_dimension[0] or y >= self.grid_dimension[1] or (x, y) in self.obstacles:
            return True
        return False

    def move_robot(self, commands):
        for command in commands:
            if command == 'R':
                self._turn_right()
            elif command == 'L':
                self._turn_left()
            elif command == 'M':
                self._move()
            else:
                raise ValueError("Invalid command")

    def get_final_position(self):
        return self.current_position

    def send_status_report(self):
        x, y, orientation = self.current_position
        obstacles_detected = "No Obstacles detected."
        if (x, y) in self.obstacles:
            obstacles_detected = "Obstacle detected."
        status_report = f"Status Report: Rover is at ({x}, {y}) facing {orientation}. {obstacles_detected}"
        return status_report
    

Grid_Size = (10, 10)
Starting_Position = (0, 0, 'N')
Commands = ['M', 'M', 'R', 'M', 'L','M']
Obstacles = [(2, 2), (3, 5)]

robot = RobotSimulator(Grid_Size, Starting_Position, Obstacles)
robot.move_robot(Commands)
final_position = robot.get_final_position()
print(final_position)

status_report = robot.send_status_report()
print(status_report)