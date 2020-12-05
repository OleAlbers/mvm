import RPi.GPIO as GPIO 
import pyaudio
import wave
import time 

# TODO: configurable
chunk=1024
sample_format=pyaudio.paInt16
channels=2
fs=44100
filename="sample.wav"
p=pyaudio.PyAudio()
stopRecording=False
isRecording=False

def rec_start():
    global stopRecording
    global isRecording
    print ("initializing recording")
    for i in range (0,5) :  
        GPIO.output(10,GPIO.HIGH) 
        time.sleep(1)
        GPIO.output(10,GPIO.LOW) 
        time.sleep(1)
    print ("starting recording")
    stream=p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames=[]

    GPIO.output(10,GPIO.HIGH) 
    isRecording=True
    while (stopRecording!=True):
        data=stream.read(chunk)
        frames.append(data)

    print ("finished recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

def rec_stop():
    global stopRecording
    stopRecording=True    
    GPIO.output(10,GPIO.LOW) 
    listen_tobutton()

def rec_callback():
    global isRecording
    if (isRecording) :
        rec_stop()
    else:
        rec_start()
    
def listen_tobutton():
    GPIO.add_event_detect (27, GPIO.RISING, callback=rec_callback)

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(10,GPIO.OUT) 
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
listen_tobutton()


while (True):
	time.sleep(1)
