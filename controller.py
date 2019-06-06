import webbrowser
import datetime, time
import os
import sys
import random
from pykeyboard import PyKeyboard
k = PyKeyboard()

def init():
	print('Heyyy familien! :)) Starter appen nuu - to sek ^^,')
	turn_off_auto_screen_blank()
	time.sleep(4)
	while True:
		check_time()

#Input
url_dict = {
	'aukinfo': 'https://aukinfo.herokuapp.com',
	'Weather Short Term': 'https://www.yr.no/sted/Norge/Tr%C3%B8ndelag/Trondheim/Trondheim/time_for_time.html',
	'Weather Long Term': 'https://www.yr.no/place/Norway/Tr%C3%B8ndelag/Trondheim/Trondheim/long.html',
}


wake_up_time = 600 #int(input('Enter Wake Up Time: '))
shut_down_time = 2200 #int(input('Enter Shut Down Time: '))
display_is_off = True




#Time keeping
def now_time():
	now_hour = datetime.datetime.now().hour
	now_min = '%02d' % datetime.datetime.now().minute
	now_time = int(str(now_hour) + str(now_min))
	return now_time


#Check if time matches set wake up time
def check_time():
	global display_is_off
	if display_is_off and wake_up_time <= now_time() < shut_down_time:
		open_web()
		time.sleep(3)
		hdmi_on()
		while(wake_up_time <= now_time() < shut_down_time):
			for i in range(0, 180):
				if not(wake_up_time <= now_time() < shut_down_time):
						break
				ctrl_tab()
				time.sleep(12)
				if i == 0:
					refresh_tab(3)
					

	if not display_is_off and now_time() >= shut_down_time:
		close_web()
		print('Klokken er ' + str(now_time()) + ' jeg tar jeg en blund - God natt :))')
		time.sleep(10)
		hdmi_off()
	success()

def open_web():
	webbrowser.get(using='chromium-browser').open('about:newtab')
	time.sleep(3)
	k.tap_key(k.function_keys[11])
	time.sleep(3)
	webbrowser.get(using='chromium-browser').open(url_dict['Weather Short Term'])
	time.sleep(3)
	webbrowser.get(using='chromium-browser').open(url_dict['Weather Long Term'])
	time.sleep(3)


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
		if i != number_of_tabs-1:
			ctrl_tab()


def close_web():
	k.press_key(k.control_l_key)
	k.tap_key('w', n=4, interval=3)
	k.release_key(k.control_l_key)


def hdmi_on():
	print('\n================================================')
	print('turning monitor on. Time is: ' + str(now_time()))
	os.system("vcgencmd display_power 1")
	global display_is_off
	display_is_off = False
	
	
def hdmi_off():
	os.system("vcgencmd display_power 0")
	global display_is_off
	display_is_off = True


def success():
	print('\n================================================')
	os.system("vcgencmd display_power 1")
	print('success!')
	sys.exit('System exit, app terminated')


def turn_off_auto_screen_blank():
	os.system('sudo xset s off')
	os.system('sudo xset -dpms')
	os.system('sudo xset s noblank')


if __name__ == "__main__":
	init()
