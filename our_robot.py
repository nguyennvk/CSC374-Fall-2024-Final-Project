import roboticstoolbox as rtb
from typing import *
from symbol import *
class OurRobot(rtb.models.Panda):
    def __init__(self, pen_position: tuple[float, float, float], paper_configure: tuple[float, float, float, float],
                 spacing: float, width: float, height: float):
        """
        :param pen_position: x, y, z position of the pen
        :param paper_configure: 4 coordinate of 4 corners of the paper
        :param spacing: space between each symbol
        :param width: width of each symbol
        :param height: height of each symbol
        """
        super().__init__()
        self.spacing = spacing
        self.pen_position = pen_position
        self.paper_configure = paper_configure
        self.width = width
        self.height = height
        self.__get_pen()
        self.__get_ready()

    def __get_ready(self):
        """
        Move the robot to the position of the paper and correct orientation. Get ready to write.
        :return:
        """
        raise NotImplementedError

    def __get_pen(self):
        """
        Using the position of the pen pick it up.
        :return:
        """
        raise NotImplementedError

    def __eval(self, expr: str) -> str:
        """
        From the expression string return the result of the calculation
        Input: "12+9-3"
        Output: "18"
        :param expr: the expression string
        :return: the result of the calculation
        """
        raise NotImplementedError

    def get_expression(self, expression: str) -> list[str]:
        """
        From the string of expression, return the list of Symbol with the result
        Input: "15+6-3"
        :param expression:
        :return:["1", "5", "+", "6", "-", "3", "=", "1", "8"]
        """
        raise NotImplementedError

    def convert_to_symbol(self, expressions: list[str]) -> list[Symbol]:
        """
        Convert the list of string to list of Symbol. Notice that the space should be counted toward the position of
        each symbol.
        :param expressions: ["1", "5", "+", "6", "-", "3", "=", "1", "8"]
        :return: [One, Five, Plus, Six, Minus, Three, Equal, "One", "Eight"]
        """
        raise NotImplementedError

    def write(self, expressions: str) -> None:
        expressions = self.get_expression(expressions)
        expressions = self.convert_to_symbol(expressions)
        for symbol in expressions:
            symbol.write()

    def terminate_task(self):
        """
        Drop the pen. To be implemented if time allowed
        :return:
        """
        raise NotImplementedError