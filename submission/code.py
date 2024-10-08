
#The program can be run again until the user decides to quit by pressing the key 'q'. Use a while loop.

import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

red = 1
green = 2
blue = 3


max_brightness = 255
while max_brightness == 255:
    try: 
        color = int(input('Select color. Press 1 for red, 2 for green or 3 for blue: '))

        for i in range(10):
            if color == 1:
                cp.pixels[i] = (max_brightness, 0, 0)
            elif color == 2:
                cp.pixels[i] = (0, max_brightness, 0)
            elif color == 3:
                cp.pixels[i] = (0, 0, max_brightness)
            else:
                print("Invalid entry")
        cp.pixels.show()
        time.sleep(0.0033)
        
        quit = input("Would you like to quit? Press q to exit or any other key to continue: ").lower()
        if quit == 'q':
            print("Program ended")
        #Turn off the leds
            for i in range(10):
                cp.pixels[i] = (max_brightness,max_brightness,max_brightness)
            max_brightness -= 1
    except:
        print('Invalid input. Try again')