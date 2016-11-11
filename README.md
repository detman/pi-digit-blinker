# pi-digit-blinker
let the raspberry blink the digits of the mathematical pi number

This is a plain stupid raspberry script

Its main purpose is to test the gpio setting and to get familiar with wiring the pi with led's - its my first raspberry hardware session.

Instead of just blinking this scripts tells us the digits of the mathematical pi number (3.1415926...) by blinking the value of each digit.

The script assumes that you wired up the GPIO 17 with an LED.
I'm using a 330 OHM resistor.
The electronic layout is
GPIO-17 > LED(+), LED(-) > 330 OHM resistor > GND

THIS SCRIPT COMES WITH NO WARRANTY

Copyright Detlef Hüttemann (c) 2016
http://www.detlef-huettemann.com
