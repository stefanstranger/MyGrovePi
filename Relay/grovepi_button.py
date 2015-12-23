from flask import Flask, render_template, request
import datetime
import grovepi
import time

#GrovePi Relay is connected on D4
relay = 4

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('start.html')

@app.route("/button", methods=['POST'])
def setRelay():
    if request.form['btnled'] == "ON":
		grovepi.pinMode(relay,"OUTPUT")
		grovepi.digitalWrite(relay,1)
		return render_template('start.html')
		#return "ON!"

    elif request.form['btnled'] == "OFF":
		grovepi.pinMode(relay,"OUTPUT")
		grovepi.digitalWrite(relay,0)
		return render_template('start.html')
		#return "OFF!"
        


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
