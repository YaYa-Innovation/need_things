from flask import Flask, jsonify, render_template
from gpiozero import CPUTemperature
import threading
import datetime
import time


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("theme1.html")
#---------------------------------------------------------------
#first thread dynamic
#----------------------------------------------------------------

def track():
	total = 0
	average = 0
	while True:
		if 1 == 1:
			average += 2
			total += 1
		x = datetime.datetime.now()
		t=(x.strftime("%I:%M:%S"))
		yield dict(total=total, average=average, t=t)

@app.route("/update")
def update():
    return jsonify(next(gen_total))
#----------------------------------------------------------------
#Second thread dynamic
#----------------------------------------------------------------

def track2():
	while True:
		rpi_temp = CPUTemperature()
		cpu=(rpi_temp.temperature)
		yield dict(cpu=cpu)

@app.route("/track2_data")
def track2_data():
	return jsonify(next(ty))

@app.route("/data")
def data():
	return render_template("theme2.html")

#----------------------------------------------------------------
#third thread dynamic text file write and read displying on html page
#----------------------------------------------------------------
def track3():
	while True:
		xq = datetime.datetime.now()
		time_now=(xq.strftime("%I:%M:%S"))
#		print("wucgwocgcgwecgwcowgco"+time_now)
		f = open("static/demofile2.txt", "w")
		f.write(time_now)
		f.close()
		f = open("static/demofile2.txt", "r")
		tt=(f.read())
		print(tt)
		yield dict(tt=tt)


@app.route("/track3_data")
def track3_data():
	return jsonify(next(ts))
#--------------------------------------------------------------

if __name__ == "__main__":
    gen_total = track()
    ty=track2()
    ts=track3()
    app.run(debug=True)


#if program already running you type this command line
#sudo ps aux | grep -i main.py
#find the Process_ID
#sudo kill -9 process_ID

