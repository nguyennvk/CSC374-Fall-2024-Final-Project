from typing import *
from our_robot import OurRobot


class Symbol:
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        """

        :param robot: the robot that write symbols
        :param position: the top left position of each symbol. Imagine that there is a rectangle surrounding the symbol
        :param width: the width of the rectangle surrounding the symbol
        :param height: the height of the rectangle surrounding the symbol
        """
        self.robot = robot
        self.position = position
        self.width = width
        self.height = height

    def write(self):
        """
        Make the robot to write the symbol. This will be implemented in the subclasses
        :return:
        """
        raise NotImplementedError

    def draw_line(self, point1: tuple[float, float, float], point2: tuple[float, float, float]):
        """
        Draw a line between two points.
        :param point1: the beginning point of the line
        :param point2: the end point of the line
        """
        raise NotImplementedError


class One(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 1 with the given width, height and position
        """


class Two(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 2 with the given width, height and position
        """


class Three(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 3 with the given width, height and position
        """


class Four(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 4 with the given width, height and position
        """


class Five(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 5 with the given width, height and position
        """


class Six(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 6 with the given width, height and position
        """


class Seven(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 7 with the given width, height and position
        """


class Eight(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 8 with the given width, height and position
        """


class Nine(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 9 with the given width, height and position
        """


class Zero(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write 0 with the given width, height and position
        """


class Plus(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write + with the given width, height and position. Try to scale down the width and height of
        plus so that it looks better
        """


class Minus(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write - with the given width, height and position. Try to scale down the width and height of
        minus so that it looks better
        """


class Multiply(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write * with the given width, height and position. Try to scale down the width and height of
        multiply so that it looks better
        """


class Divide(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write / with the given width, height and position. Try to scale down the width and height of
        divide so that it looks better
        """


class Equal(Symbol):
    def __init__(self, robot: OurRobot, position: tuple[float, float, float], width: float, height: float):
        super().__init__(robot, position, width, height)

    def write(self):
        """
        Make the robot to write + with the given width, height and position. Try to scale down the width and height of
        equal so that it looks better
        """
