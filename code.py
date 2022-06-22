print("Hello World!")
import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio
import microcontroller


mouse = Mouse(usb_hid.devices) #mouse func. definition
led = digitalio.DigitalInOut(board.GP25) #led defined
led.direction = digitalio.Direction.OUTPUT #led value


led.value = False #Do you want activate led?
time.sleep(0) #You can set bigger than 0 if you want wait before cycle
depth=5 #Movement area
betw=120 #Time between movements
wait=120 #Wait time for restart Cycle


while True:
	print("Controller is", microcontroller.cpu.temperature, "°C") #Celcius value of device cpu
	led.value = not led.value
	mouse.move(x=depth)
	#mouse.move(y=depth)
	led.value = not led.value
	print(betw ,"sec wait")
	time.sleep(betw)
	led.value = not led.value
	mouse.move(x=-depth)
	#mouse.move(y=-depth)
	led.value = not led.value
	print("time is up, cycle restarting after", wait, "second")
	time.sleep(wait)
