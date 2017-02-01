import time as t
from robot import Robot


def main():
    left_threshold = 0 #  Edit this with sensor values
    center_threshold = 0  # Edit this with sensor values
    right_threshold = 0  # Edit this with sensor values

    robot = Robot()
    robot.open()

    while True:
        try:
            d_left, d_center, d_right = robot.read()

            if d_center < center_threshold or (d_left < left_threshold and d_right < right_threshold):
                robot.move_backwards()
            elif d_left < left_threshold:
                robot.turn_right()
            elif d_right < right_threshold:
                robot.turn_left()
            else:
                robot.move_forward()

            t.sleep(0.2)

        except KeyboardInterrupt:
            robot.stop()
            robot.close()
            break


if __name__ == '__main__':
    main()
