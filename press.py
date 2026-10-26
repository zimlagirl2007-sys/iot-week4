from gpiozero import Button
from time import sleep

button = Button(27)	# internal pull-up enabled; button wired to GND

while True:
	if button.is_pressed:
		print("pressed")
	else:
		print("released")
	sleep(0.2)

