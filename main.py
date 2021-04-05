#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#initialze the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#intialize the ultrasonic sesonr
obstacle_sensor = UltrasonicSensor(Port.S4)

#initliaze the driver base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#play sound when starting


while True:

    robot.drive(500, 0)

    while obstacle_sensor.distance() > 300:
        wait(10)
        if obstacle_sensor.distance() > 300:
            ev3.speaker.play_file(SoundFile.CONFIRM)

        robot.straight(-300)
        robot.turn(120)




