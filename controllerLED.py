from gpiozero import LED
from time import sleep
import threading
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

green = LED(17)
yellow = LED(27)
red = LED(22)

jobs = []
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
		if (stop == True):
			break
	return
			

	
	
@app.route("/")
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
	task1 = threading.Thread(target=cycle)
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
	
	
	
	
