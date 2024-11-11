import roboticstoolbox as rtb
import swift
import numpy as np
import time
from math import pi
from spatialmath import SE3
import spatialgeometry as sg
from our_robot import *
from symbol import *


pen_x, pen_y, pen_z = 1, 1, 1
paper_TL, paper_TR, paper_BL, paper_BR = 1, 2, 3, 4
space = 0.5
width = 1
height = 1

our_robot = OurRobot((pen_x, pen_y, pen_z), (paper_TL, paper_TR, paper_BL, paper_BR), space,
                     width, height)

user_input = input("Enter your expression with (+ - * /) or q to quit: ")
while user_input != "q":
    our_robot.write(user_input)
