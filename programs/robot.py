class Robot(object):
    def __init__(self):
        pass

    def open(self, d=None):
        pass

    def close(self):
        pass

    def move_forward(self, velocity=None):
        print('Moving forward with velocity: {}'.format(velocity))

    def move_backwards(self, velocity=None):
        print('Moving backwards with velocity: {}'.format(velocity))

    def turn_left(self, velocity=None):
        print('Turning left with velocity: {}'.format(velocity))

    def turn_right(self, velocity=None):
        print('Turning right with velocity: {}'.format(velocity))

    def read(self):
        """
        Read the robot's distance sensors
        :return: d_left, d_center, d_right
        """
        return None, None, None