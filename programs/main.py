from .robot import Robot


def main():
    robot = Robot()
    robot.open()

    robot.move_forward()


if __name__ == '__main__':
    main()
    