from gpiozero import LED
from time import sleep

led = LED(17)		#BCM number: GPI017, the wire on physical pin 11

for n in range(10):
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)
	print(f"blink {n}")

