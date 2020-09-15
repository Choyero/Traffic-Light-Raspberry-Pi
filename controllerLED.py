from gpiozero import LED #include gpio library to control our leds
from time import sleep
import threading #include threading so that we can start the cycle without looping forever waiting for it to end
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

#set uo led pins
green = LED(17)
yellow = LED(27)
red = LED(22)

jobs = []
#flag so that we can stop the thread 
stop = False

def greenOn():
	green.on()


def greenOff():
	green.off()
		
def yellowOn():
	
	yellow.on()


def yellowOff():
	
	yellow.off()	
		
		
		
def redOn():
	
	red.on()


def redOff():
	
	red.off()
		

def cycle():
	global stop
	stop = False
	greenOff()
	yellowOff()
	redOff()
	while True:
		greenOn()
		sleep(1)
		greenOff()
		yellowOn()
		sleep(1)
		yellowOff()
		redOn()
		sleep(1)
		redOff()
		if (stop == True): #break if stop cycle button has been clicked
			break
	return
			

	
	
@app.route("/")# give us the page found in templates index.html
def index():
	return render_template(
    'index.html')
    
@app.route("/greenon")
def greenON():
	greenOn()
	return render_template(
    'index.html')
    
@app.route("/greenoff")
def greenOFF():
	greenOff()
	return render_template(
    'index.html')
    
@app.route("/yellowon")
def yellowON():
	yellowOn()
	return render_template(
    'index.html')
    
@app.route("/yellowoff")
def yellowOFF():
	yellowOff()
	return render_template(
    'index.html')
    
@app.route("/redon")
def redON():
	redOn()
	return render_template(
    'index.html')
    
@app.route("/redoff")
def redOFF():
	redOff()
	return render_template(
    'index.html')

@app.route("/cycle")
def CYCLE():
	global jobs 
	task1 = threading.Thread(target=cycle) # create a thread
	jobs.append('task1')
	task1.start()
	return render_template(
    'index.html')
	
@app.route("/stop")
def stopcycle():
	global stop
	stop = True
	return render_template(
    'index.html')


if __name__ == "__main__":
    app.run(threaded=True)
	
	
	
	
