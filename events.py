from gpiozero import Button 
from signal import pause

def hello():
	print("pressed!")

button = Button(27, bounce_time=0.05)
button.when_pressed = hello	# the function itself, no paentheses

pause()		# sleep forever; events do the work

