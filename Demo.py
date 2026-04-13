# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep
import curses
#define the pin for drv8833#1
NSLEEP1 = 12  #Enabling signal pin for drv8833
AN11 = 17
AN12 = 27
BN11 = 22
BN12 = 23
#define the pin for drv8833#2
NSLEEP2 = 13
AN21 = 24
AN22 = 25
BN21 = 26
BN22 = 16
temp1=1

GPIO.setmode(GPIO.BCM)
#Define pin as output signal
GPIO.setup(NSLEEP1,GPIO.OUT)
GPIO.setup(NSLEEP2,GPIO.OUT)
GPIO.setup(AN11,GPIO.OUT)
GPIO.setup(AN12,GPIO.OUT)
GPIO.setup(BN11,GPIO.OUT)
GPIO.setup(BN12,GPIO.OUT)
GPIO.setup(AN21,GPIO.OUT)
GPIO.setup(AN22,GPIO.OUT)
GPIO.setup(BN21,GPIO.OUT)
GPIO.setup(BN22,GPIO.OUT)
#Initialize the motor drive signal so that the motor is in a stopped state
GPIO.output(AN11,GPIO.LOW)
GPIO.output(AN12,GPIO.LOW)
GPIO.output(BN11,GPIO.LOW)
GPIO.output(BN12,GPIO.LOW)
GPIO.output(AN21,GPIO.LOW)
GPIO.output(AN22,GPIO.LOW)
GPIO.output(BN21,GPIO.LOW)
GPIO.output(BN22,GPIO.LOW)
p1=GPIO.PWM(NSLEEP1,1000)#Define p1 as a pulse signal of 1000 Hz
p2=GPIO.PWM(NSLEEP2,1000)#Define p2 as a pulse signal of 1000 Hz
p1.start(70)#P1 defaults to a duty cycle of 70%
p2.start(70)#P2 defaults to a duty cycle of 70%

# Curses Setup for keyboard input
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)  # make getch non-blocking

p1.ChangeDutyCycle(90)#Set the P1 pulse signal duty cycle to 90%
p2.ChangeDutyCycle(90)#Set the P2 pulse signal duty cycle to 90%
clawStatus=0
try:
    while True:
        char = screen.getch()
        if char == -1:
            # No key pressed: ensure all motor control pins are LOW
            GPIO.output(AN11,GPIO.LOW)
            GPIO.output(AN12,GPIO.LOW)
            GPIO.output(BN11,GPIO.LOW)
            GPIO.output(BN12,GPIO.LOW)
            GPIO.output(AN21,GPIO.LOW)
            GPIO.output(AN22,GPIO.LOW)
            GPIO.output(BN21,GPIO.LOW)
            GPIO.output(BN22,GPIO.LOW)
        elif char == curses.KEY_RIGHT:
            GPIO.output(AN11,GPIO.LOW)
            GPIO.output(AN12,GPIO.HIGH)
            #GPIO.output(BN11,GPIO.LOW)
            #GPIO.output(BN12,GPIO.HIGH)
            #GPIO.output(AN21,GPIO.LOW)
            #GPIO.output(AN22,GPIO.HIGH)
            #GPIO.output(BN21,GPIO.LOW)
            #GPIO.output(BN22,GPIO.HIGH)
        elif char == curses.KEY_LEFT:
            GPIO.output(AN11,GPIO.HIGH)
            GPIO.output(AN12,GPIO.LOW)
            #GPIO.output(BN11,GPIO.LOW)
            #GPIO.output(BN12,GPIO.HIGH)
            #GPIO.output(AN21,GPIO.LOW)
            #GPIO.output(AN22,GPIO.HIGH)
            #GPIO.output(BN21,GPIO.LOW)
            #GPIO.output(BN22,GPIO.HIGH)
        elif char == curses.KEY_UP:
            #GPIO.output(AN11,GPIO.HIGH)
            #GPIO.output(AN12,GPIO.LOW)
            GPIO.output(BN11,GPIO.HIGH)
            GPIO.output(BN12,GPIO.LOW)
            #GPIO.output(AN21,GPIO.HIGH)
            #GPIO.output(AN22,GPIO.LOW)
            #GPIO.output(BN21,GPIO.HIGH)
            #GPIO.output(BN22,GPIO.LOW)
        elif char == curses.KEY_DOWN:
            #GPIO.output(AN11,GPIO.HIGH)
            #GPIO.output(AN12,GPIO.LOW)
            GPIO.output(BN11,GPIO.LOW)
            GPIO.output(BN12,GPIO.HIGH)
            #GPIO.output(AN21,GPIO.HIGH)
            #GPIO.output(AN22,GPIO.LOW)
            #GPIO.output(BN21,GPIO.HIGH)
            #GPIO.output(BN22,GPIO.LOW)
        sleep(0.02)  # small delay to avoid busy loop
except KeyboardInterrupt:
    pass
finally:
    # Restore terminal state
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()
    # Stop PWMs and cleanup GPIO
    try:
        p1.stop()
        p2.stop()
    except Exception:
        pass
    GPIO.cleanup()

