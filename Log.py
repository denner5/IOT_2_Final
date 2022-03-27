import sqlite3
import RPi.GPIO as GPIO
from datetime import datetime

#import subprocess as ap
class data:
    motion = 0
    button = 0

dbname='Sensordata.db'
sampleFreq = 1 # time in seconds


# get data from DHT sensor
def getButtondata():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    button = 20
    senPIR = 16

    # Set button and PIR sensor pins as an input
    GPIO.setup(button, GPIO.IN)
     #motion sensor
    GPIO.setup(senPIR, GPIO.IN)


    if GPIO.input(20) == GPIO.HIGH:
        print(" trykket")
        #print(GPIO.input(20))
        #webbrowser.open(url, new)
        #time.sleep(160)
        #webbrowser.close()
        data.button = 1


    else:
        print("ikke trykket")
        print(GPIO.input(20))
        data.button = 0

def getMotiondata():
  #sensor
    if GPIO.input(16) == GPIO.HIGH :
        print("Bevægelse")
        #webbrowser.open(url1,new)
        data.motion = 1
        #GPIO.output(26,GPIO.LOW)
    else:
        print("Stille")
        data.motion = 0

# log sensor data on database
def logData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO Sensor_data values(datetime('now'), (?), (?))", (data.button, data.motion))
    conn.commit()
    conn.close()
