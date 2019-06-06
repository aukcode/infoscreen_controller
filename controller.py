import webbrowser
import datetime, time
import os
import sys
import random
from pykeyboard import PyKeyboard
k = PyKeyboard()

def init():
	#print('Turning off HDMI...')
	time.sleep(2)
	#hdmi_off()
	turn_off_auto_screen_blank()
	#prevent_evening_or_weekend_trigger()
	while True:
		#if weekday, run app (saturday is 5)
		if datetime.datetime.now().weekday() < 6:
			check_time()
		else:
			prevent_evening_or_weekend_trigger()


#Input
url_dict = {
	'aukinfo': 'https://aukinfo.herokuapp.com',
	'Calendar': 'https://www.calendar.google.com/calendar/r',
	'Weather Short Term': 'https://www.yr.no/place/Norway/Trondelag/Trondheim/Trondheim/hour_by_hour.html',
	'Weather Long Term': 'https://www.yr.no/place/Norway/Trondelag/Trondheim/Trondheim/long.html',
	}


wake_up_time = 600 #int(input('Enter Wake Up Time: '))
shut_down_time = 2200 #int(input('Enter Shut Down Time: '))
display_is_off = True


def turn_off_auto_screen_blank():
	os.system('sudo xset s off')
	os.system('sudo xset -dpms')
	os.system('sudo xset s noblank')


#Time keeping
def now_time():
	now_hour = datetime.datetime.now().hour
	now_min = '%02d' % datetime.datetime.now().minute
	now_time = int(str(now_hour) + str(now_min))
	return now_time


def prevent_evening_or_weekend_trigger():
	print('Preventing evening trigger')
	while now_time() >= shut_down_time or datetime.datetime.now().weekday() >= 5:
		time.sleep(10)


#Check if time matches set wake up time
def check_time():
	#print('runnning check_time')
	global display_is_off
	if display_is_off and wake_up_time <= now_time() < shut_down_time:
		print('\n================================================')
		print('waking up')
		#hdmi_on()
		time.sleep(3)
		while(True):
			for i in range(0, 180):
				ctrl_tab()
				time.sleep(12)
				if i == 0:
					refresh_tab(3)

	if not display_is_off and now_time() >= shut_down_time:
		close_web()
		print('going to sleep in 10 sek')
		time.sleep(10)
		hdmi_off()


def hdmi_on():
	print('turning monitor on. Time is: ' + str(now_time()))
	os.system("tvservice -p")
	global display_is_off
	display_is_off = False


def open_web():
	webbrowser.get(using='chromium-browser').open(url_dict['Calendar'])
	time.sleep(3)
	#webbrowser.get(using='chromium-browser').open(url_dict['Weather Long Term'])
	time.sleep(3)
	k.tap_key(k.function_keys[11])


def ctrl_tab():
	time.sleep(1) #PI is slow
	k.press_key(k.control_l_key)
	time.sleep(1)
	k.tap_key(k.tab_key)
	k.release_key(k.control_l_key)


def refresh_tab(number_of_tabs):
	for i in range(0, number_of_tabs):
		k.press_key(k.control_l_key)
		time.sleep(1)
		k.tap_key('r')
		k.release_key(k.control_l_key)
		time.sleep(1)
		ctrl_tab()

def close_web():
	k.press_key(k.control_l_key)
	k.tap_key('w', n=4, interval=3)
	k.release_key(k.control_l_key)


def hdmi_off():
	os.system("tvservice -o")
	global display_is_off
	display_is_off = True


def success():
	print('\n================================================')
	os.system("tvservice -p")
	print('success!')
	sys.exit('System exit, app terminated')


if __name__ == "__main__":
	init()
