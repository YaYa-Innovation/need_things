from flask import Flask, jsonify, render_template
from gpiozero import CPUTemperature
import datetime
import time


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("theme1.html")
#---------------------------------------------------------------
#first thread dynamic
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
#third thread dynamic
def track3():
	while True:
		xq = datetime.datetime.now()
		tt=(xq.strftime("%I:%M:%S"))
		print (tt)
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
