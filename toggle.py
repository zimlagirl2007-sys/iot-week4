from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(27, bounce_time=0.05)

button.when_pressed = led.toggle	# each press flips the LED

pause()
