import webbrowser
import time
from pynput.keyboard import Key, Controller

def open_site():
    #enter ip address of camers
    a_website = "http://admin:@10.0.0.5/video/livemb.asp"
     
    # Open url in a new window of the default browser, if possible
    webbrowser.open_new(a_website)
open_site()
def full_screen():
    time.sleep(15)
    keyboard = Controller()
    time.sleep(3)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
full_screen()


