class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.face = None
        self.table_size = 5

    def place(self, x, y, face):
        if self.is_valid_position(x, y):
            self.x = x
            self.y = y
            self.face = face
        else:
            print("Position not valid")

    def move(self):
        if self.face == "NORTH" and self.is_valid_position(self.x, self.y + 1):
            self.y += 1
        elif self.face == "SOUTH" and self.is_valid_position(self.x, self.y - 1):
            self.y -= 1
        elif self.face == "EAST" and self.is_valid_position(self.x + 1, self.y):
            self.x += 1
        elif self.face == "WEST" and self.is_valid_position(self.x - 1, self.y):
            self.x -= 1
        else: 
            print("Position not valid")

    def left(self):
        directions = ["NORTH", "WEST", "SOUTH", "EAST"]
        current_index = directions.index(self.face)
        self.face = directions[(current_index - 1) % 4]

    def right(self):
        directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        current_index = directions.index(self.face)
        self.face = directions[(current_index + 1) % 4]

    def report(self):
        return f"Current position: {self.x},{self.y},{self.face}"

    def is_valid_position(self, x, y):
        return 0 <= x < self.table_size and 0 <= y < self.table_size
        


def process_command(command, robot):
    if command.startswith("PLACE"):
        _, position = command.split(" ")
        x, y, face = map(str, position.split(","))
        robot.place(int(x), int(y), face)
    elif command == "MOVE":
        robot.move()
    elif command == "LEFT":
        robot.left()
    elif command == "RIGHT":
        robot.right()
    elif command == "REPORT":
        print(robot.report())


if __name__ == "__main__":
    robot = ToyRobot()

    while True:
        user_input = input("Enter command: ")
        process_command(user_input, robot)
