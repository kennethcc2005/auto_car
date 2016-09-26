import pygame
from pygame.locals import *
import time
import sys, tty, termios, os
import RPi.GPIO as io

class RCTest(object):

    def __init__(self):
        

        io.setmode(io.BCM)

        # Constant values
        # PWM_MAX                 = 100

        # Disable warning from GPIO
        io.setwarnings(False)

        # Here we configure the GPIO settings for the left and right motors spinning direction. 
        # It defines the four GPIO pins used as input on the L298 H-Bridge to set the motor mode (forward, reverse and stopp).

        #Steering Motor
        self.leftmotor_in1_pin = 27
        self.leftmotor_in2_pin = 22
        io.setup(self.leftmotor_in1_pin, io.OUT)
        io.setup(self.leftmotor_in2_pin, io.OUT)

        #Foward/Backward Motor
        self.rightmotor_in1_pin = 24
        self.rightmotor_in2_pin = 25
        io.setup(self.rightmotor_in1_pin, io.OUT)
        io.setup(self.rightmotor_in2_pin, io.OUT)

        io.output(self.leftmotor_in1_pin, False)
        io.output(self.leftmotor_in2_pin, False)
        io.output(self.rightmotor_in1_pin, False)
        io.output(self.rightmotor_in2_pin, False)
        pygame.init()
        screen = pygame.display.set_mode((468, 60))
        pygame.display.set_caption('Monkey Fever')
        pygame.mouse.set_visible(0)
        self.send_inst = True
        self.steer()

        # Here we configure the GPIO settings for the left and right motors spinning speed. 
        # It defines the two GPIO pins used as input on the L298 H-Bridge to set the motor speed with a PWM signal.

        # leftmotorpwm_pin = 4
        # rightmotorpwm_pin = 17

        # io.setup(leftmotorpwm_pin, io.OUT)
        # io.setup(rightmotorpwm_pin, io.OUT)

        # leftmotorpwm = io.PWM(leftmotorpwm_pin,100)
        # rightmotorpwm = io.PWM(rightmotorpwm_pin,100)

        # leftmotorpwm.start(0)
        # leftmotorpwm.ChangeDutyCycle(0)

        # rightmotorpwm.start(0)
        # rightmotorpwm.ChangeDutyCycle(0)


    def setMotorMode(self,motor, mode):

    # setMotorMode()

    # Sets the mode for the L298 H-Bridge which motor is in which mode.

    # This is a short explanation for a better understanding:
    # motor     -> which motor is selected left motor or right motor
    # mode      -> mode explains what action should be performed by the H-Bridge

    # setMotorMode(leftmotor, reverse)  -> The left motor is called by a function and set into reverse mode
    # setMotorMode(rightmotor, stopp)   -> The right motor is called by a function and set into stopp mode

        if motor == "steermotor":
            if mode == "left":
                io.output(self.leftmotor_in1_pin, True)
                io.output(self.leftmotor_in2_pin, False)
            elif  mode == "right":
                io.output(self.leftmotor_in1_pin, False)
                io.output(self.leftmotor_in2_pin, True)
            else:
                io.output(self.leftmotor_in1_pin, False)
                io.output(self.leftmotor_in2_pin, False)
                
        elif motor == "powermotor":
            if mode == "reverse":
                io.output(self.rightmotor_in1_pin, True)
                io.output(self.rightmotor_in2_pin, False)     
            elif  mode == "forward":
                io.output(self.rightmotor_in1_pin, False)
                io.output(self.rightmotor_in2_pin, True)        
            else:
                io.output(self.rightmotor_in1_pin, False)
                io.output(self.rightmotor_in2_pin, False)
        else:
            io.output(self.leftmotor_in1_pin, False)
            io.output(self.leftmotor_in2_pin, False)
            io.output(self.rightmotor_in1_pin, False)
            io.output(self.rightmotor_in2_pin, False)



    def setMotorSteer(self,power):

    # SetMotorLeft(power)

    # Sets the drive level for the left motor, from +1 (max) to -1 (min).

    # This is a short explanation for a better understanding:
    # SetMotorLeft(0)     -> left motor is stopped
    # SetMotorLeft(0.75)  -> left motor moving forward at 75% power
    # SetMotorLeft(-0.5)  -> left motor moving reverse at 50% power
    # SetMotorLeft(1)     -> left motor moving forward at 100% power
        if power < 0:
            # Reverse mode for the left motor
            self.setMotorMode("steermotor", "left")
            # pwm = -int(PWM_MAX * power)
            # if pwm > PWM_MAX:
            #     pwm = PWM_MAX
        elif power > 0:
            # Forward mode for the left motor
            self.setMotorMode("steermotor", "right")
            # pwm = int(PWM_MAX * power)
            # if pwm > PWM_MAX:
            #     pwm = PWM_MAX
        else:
            # Stopp mode for the left motor
            self.setMotorMode("steermotor", "stop")
            # pwm = 0
    #   print "SetMotorLeft", pwm
        # leftmotorpwm.ChangeDutyCycle(pwm)

    def setMotorPower(power):

    # SetMotorRight(power)

    # Sets the drive level for the right motor, from +1 (max) to -1 (min).

    # This is a short explanation for a better understanding:
    # SetMotorRight(0)     -> right motor is stopped
    # SetMotorRight(0.75)  -> right motor moving forward at 75% power
    # SetMotorRight(-0.5)  -> right motor moving reverse at 50% power
    # SetMotorRight(1)     -> right motor moving forward at 100% power

        if power < 0:
            # Reverse mode for the right motor
            self.setMotorMode("powermotor", "reverse")
            # pwm = -int(PWM_MAX * power)
            # if pwm > PWM_MAX:
            #     pwm = PWM_MAX
        elif power > 0:
            # Forward mode for the right motor
            self.setMotorMode("powermotor", "forward")
            # pwm = int(PWM_MAX * power)
            # if pwm > PWM_MAX:
            #     pwm = PWM_MAX
        else:
            # Stopp mode for the right motor
            self.setMotorMode("powermotor", "stop")

    def steer(self):
        while self.send_inst:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print("Forward Right")
                        # powermotor = min(1, powermotor+1)
                        # steermotor = min(1, steermotor+1)
                        self.setMotorPower(1)
                        self.setMotorSteer(1)

                    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                        print("Forward Left")
                        # powermotor = min(1, powermotor+1)
                        # steermotor = max(-1, steermotor-1)
                        self.setMotorPower(1)
                        self.setMotorSteer(-1)

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                        print("Reverse Right")
                        # powermotor = max(-1, powermotor-1)
                        # steermotor = min(1, steermotor+1)
                        self.setMotorPower(-1)
                        self.setMotorSteer(1)

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                        print("Reverse Left")
                        # powermotor = max(-1, powermotor-1)
                        # steermotor = max(-1, steermotor-1)
                        self.setMotorPower(-1)
                        self.setMotorSteer(-1)

                    # simple orders
                    elif key_input[pygame.K_UP]:
                        print("Forward")
                        # powermotor = min(1, powermotor+1)
                        self.setMotorPower(1)
                        self.setMotorSteer(0)

                    elif key_input[pygame.K_DOWN]:
                        print("Reverse")
                        # powermotor = max(-1, powermotor-1)
                        self.setMotorPower(-1)
                        self.setMotorSteer(0)

                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                        # steermotor = min(1, steermotor+1)
                        self.setMotorPower(0)
                        self.setMotorSteer(1)

                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                        # steermotor = max(-1, steermotor-1)
                        self.setMotorPower(0)
                        self.setMotorSteer(-1)

                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print 'Exit'
                        self.send_inst = False
                        powermotor = 0
                        steermotor = 0
                        self.setMotorPower(powermotor)
                        self.setMotorSteer(steermotor)
                        exit()
                        break

                elif event.type == pygame.KEYUP:
                    powermotor = 0
                    steermotor = 0
                    self.setMotorPower(powermotor)
                    self.setMotorSteer(steermotor)

if __name__ == '__main__':
    RCTest()
