import RPi.GPIO as GPIO
from time import sleep

direction = True #Direction of rotation of the Motor. True => Moving forward. False => Moving backwards

GPIO.setmode(GPIO.BCM) #GPIO Mode

GPIO.setup(25, GPIO.OUT) #Setting up the ENA pin

GPIO.setup(23, GPIO.OUT) #Setting up the IN1 pin
GPIO.setup(24, GPIO.OUT) #Setting up the IN2 pin

#Setting both input pins to 0 (default state of the motor is "stopped")
GPIO.output(23, GPIO.LOW) 
GPIO.output(24, GPIO.LOW)

#Setting the ENA signal to a PWM signal with a 1KHz frequency.
p = GPIO.PWM(25, 1000)

#Starting the PWM signal with a 25% Duty Cycle
p.start(25)

while(1):
	print("Available commands are as follows (non case-sensitive): (R)un\n(S)top\n(F)orward\n(B)ackward\n(Slow)\n(Fast)\n(E)xit\n")
	command = input("Please input a command: ")
	
  #Run command
	if lower(command) == 'r':
		print("Your input is: Run")
		if direction:
			GPIO.output(23, GPIO.HIGH)
			GPIO.output(24, GPIO.LOW)
		else:
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.HIGH)
  
  #Slow command
	elif lower(command) == 'slow':
		print("Your input is: Slow")
		p.ChangeDutyCycle(30)
  #Fast command
	elif lower(command) == 'fast':
		print("Your input is: Fast")
		p.ChangeDutyCycle(80)		
  #Stop command
	elif lower(command[0]) == 's':
		print("Your input is: Stop")
		GPIO.output(23, GPIO.LOW) 
		GPIO.output(24, GPIO.LOW)
  #Forward command
	elif lower(command[0]) == 'f':
		print("Your input is: Forward")
		direction = True
		GPIO.output(23, GPIO.HIGH)
		GPIO.output(24, GPIO.LOW)
  #Backward command
	elif lower(command[0]) == 'b':
		print("Your input is: Backward")
		direction = False
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
  #Exit command
	elif lower(command[0]) == 'e':
		print("Your input is: Exit")
		GPIO.cleanup()
		break	
	
	else:
		print("Invalid Input")
		print("Please enter one of the commands listed below:\n")
	
	
