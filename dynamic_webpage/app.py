import time
import threading
from flask import Flask, render_template
import datetime
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
	print(test)
	templateData ={
		'test':test
	}
	return render_template('index.html',**templateData)

@app.route('/page')
def page():
	return "hello"

def web():
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

def usb():
	while True:
		global test
		x = datetime.datetime.now()
		test=(x.strftime("%I:%M:%S"))
		print(test)
		time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=usb, daemon=True).start()
    threading.Thread(target=web, daemon=True).start()
    while True:
        time.sleep(1)









#if program already running you type this command line
#sudo ps aux | grep -i app.py
#find the Process_ID
#sudo kill -9 process_ID
