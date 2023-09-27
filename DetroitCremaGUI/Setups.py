import time
# import board
# import busio
# import digitalio
import threading
import numpy as np
# import RPi.GPIO as GPIO
from threading import Thread
import matplotlib.pyplot as plt
# from scipy.signal import butter,filtfilt
# import adafruit_ads1x15.ads1115 as ADS
# from adafruit_ads1x15.analog_in import AnalogIn
# from adafruit_ads1x15.ads1x15 import Mode
# import adafruit_max31856
# from hx711 import HX711
import PlotEspressoProfile as prof

'''
print('Begin Setup')
#set up HX711
hx = HX711(5,6)
hx.reset()
hx.set_gain(128)
init_calib = [0,0,0,0,0,]
for i in range(5):
    init_calib[i] = hx.get_value(5)
offset = np.average(init_calib)
hx.set_offset(offset)
print('Offset: {}'.format(offset))
raw_to_gram = 794
print(hx.get_weight(1))

print('Setting Up ADS')

#set up ads1115
RATE = 860
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)
mode = Mode.CONTINUOUS
ads.data_rate = RATE

print('Setting Up Pump')
#set up pump
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
sol = digitalio.DigitalInOut(board.D19)
sol.direction = digitalio.Direction.OUTPUT
sol.value = True

print('Set Up MAX31856')
#set up max31856 
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D25)
cs.direction = digitalio.Direction.OUTPUT
thermocouple = adafruit_max31856.MAX31856(spi, cs)
thermocouple.auto_convert = True
rel = digitalio.DigitalInOut(board.D26)
rel.direction = digitalio.Direction.OUTPUT
rel.value = False
'''
print('Setting Vars')
# Variables
pumpOn = False
new_period = True
heat_up_flag = False
infuse_flag = False
preinfuse_time = 0
preinfuse_bar = 0
brew_time = 0
targ_weight = 0
raw_pressure = 0
pressure = 0
prev_pressure = 0
expected_pressure = 0
weight = 0
temp = 0 #thermocouple.temperature
targ_temp = 80
counter = 0
click = 0
cps = 1
cps_T = 1
cps_quick = 0
delta_cps = 0
delta_cps_T = 0
error = 0
avg_val = 0
avg_cntr = 0
delta_t = 0
prev_loop_time_P = 0
prev_loop_time_T = 0
loop_end = 0
weight_list = []
raw_pressure_list = []
pressure_list = []
expected_pressure_list = []
elapsedTime_list = []
cps_list = []
cps_temp_list = []
delta_cps_list = []
delta_cps_list_T = []
temp_list = []
targ_pressure_arr = [0,0,0,0,0]
targ_time_arr = [0,0,0,0,0]
loops = 0


print('Starting Plot Script')
# Create profile and respective vars
profile = prof.ProfilePlot()
'''x = np.array([0,10,20,22,24,26,30])
y = np.array([0,0,0,0,0,0,0])
profile.create_plot(x,y)
#targ1 = profile.getPressureTarg(0)
#targ2 = profile.getPressureTarg(1)
#targ3 = profile.getPressureTarg(2)'''
'''
print('Creating zc function')
#zc call back function
def check_zero_crossing(channel):
	global counter, new_period
	if new_period:
		if pumpOn:
			GPIO.output(13, GPIO.HIGH)
		if not pumpOn:
			GPIO.output(13, GPIO.LOW)
	new_period = not new_period

print('Make event detect')

# Create ZC detection event and temp thread
GPIO.add_event_detect(16, GPIO.FALLING, callback = check_zero_crossing)
'''
# Create timer vars
startTime = 0
elapsedTime = 0
endTime = 0

print("Setup Complete")
