# Control 4 pin LED Stripe (red, green, blue, power)
from machine import Pin, PWM
from src.db import db

RED_PIN = 8
GREEN_PIN = 5
BLUE_PIN = 4

red = PWM(Pin(RED_PIN, mode=Pin.OUT))
green = PWM(Pin(GREEN_PIN, mode=Pin.OUT))
blue = PWM(Pin(BLUE_PIN, mode=Pin.OUT))
pwmGround = Pin(18, mode=Pin.OUT)

# Freq: 7 - 125_000_000 (Hz)
red.freq(10_000)
green.freq(10_000)
blue.freq(10_000)


def pwmLedSetColor(redValue: int, greenValue: int, blueValue: int):
    '''
      Input range 0-255
    '''
    try:
        db('SAVE', 'pwmRedValue', redValue)
        db('SAVE', 'pwmGreenValue', greenValue)
        db('SAVE', 'pwmBlueValue', blueValue)

        redValue = int(redValue * 257)
        greenValue = int(greenValue * 257)
        blueValue = int(blueValue * 257)

        red.duty_u16(redValue)
        green.duty_u16(greenValue)
        blue.duty_u16(blueValue)
    except:
        pass

    return


def pwmEnable():
    pwmGround.value(1)
    db('SAVE', 'pwmStatus', 1)


def pwmDisable():
    pwmGround.value(0)
    db('SAVE', 'pwmStatus', 0)
