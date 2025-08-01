from machine import Pin,PWM,ADC
from time import sleep

servo = PWM(Pin(0))#include the servo motor pin
potentiometer = ADC(28)
servo.freq(50)

in_min = 0
in_max = 65535

out_min = 1000
out_max = 9000

while True:
    #Get the potentiometer values
    value = potentiometer.read_u16()
    #Convert PWM values from 0 to 180
    Servo_value = (value - in_min)*(out_max - out_min)/(in_max - in_min) + out_min
    servo.duty_u16(int(Servo_value))
