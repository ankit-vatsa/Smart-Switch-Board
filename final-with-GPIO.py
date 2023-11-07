import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer

#define BLYNK_TEMPLATE_ID "_enterID_"
#define BLYNK_TEMPLATE_NAME "SmartSwitchBoard"
#define BLYNK_AUTH_TOKEN "_____enterID_____"
BLYNK_AUTH_TOKEN = "_____enterID_____"

led1 = 18
led2 = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

x=20
# Turn on the device
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)


kill_switch_state = False


@blynk.on("V0")
def ankit_switch_handler(value):
#    global led_switch
    global kill_switch_state
    if int(value[0]) == 1:
        print('Kill Switch in action.\nAll switches are turned OFF.')
        kill_switch_state = True
        blynk.virtual_write(1,0)
        blynk.virtual_write(2,0)  
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
    else:
        print('Kill Switch is now OFF.')
        kill_switch_state = False
#        subprocess.run(["sudo","shutdown","now"])#to turn off RaspberryPi


@blynk.on("V1")
def v0_write_handler(value):
#    global led_switch
    global kill_switch_state
    if int(value[0]) == 1 and not kill_switch_state:
        GPIO.output(led1, GPIO.HIGH)
        print('Light 1 is ON')
        quit
    else:
        blynk.virtual_write(1,0)
        GPIO.output(led1, GPIO.LOW)
        print('Light 1 is OFF')
@blynk.on("V2")
def v0_write_handler(value):
#    global led_switch
    if int(value[0]) == 1 and not kill_switch_state:
        GPIO.output(led2, GPIO.HIGH)
        print('Light 2 is ON')
        quit
    else:
        blynk.virtual_write(2,0)
        GPIO.output(led2, GPIO.LOW)
        print('Light 2 is OFF')
# Initialize Blynk


#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
  print("Mr. Ankit Vatsa, Thankyou for using Blynk.Edge.\nRaspberry Pi Connected to New Blynk.")


while True:
  blynk.run()
