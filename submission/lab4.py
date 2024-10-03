
#The program can be run again until the user decides to quit by pressing the key 'q'. Use a while loop.

import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

red = 1
green = 2
blue = 3

#This is the control variable
max_brightness = 255

#Entering the while loop
while max_brightness == 255:
    try: 
        color = int(input('Select color. Press 1 for red, 2 for green or 3 for blue: '))

        for i in range(10):
            #This is the if else statements to choose colors
            if color == 1:
                cp.pixels[i] = (max_brightness, 0, 0)
            elif color == 2:
                cp.pixels[i] = (0, max_brightness, 0)
            elif color == 3:
                cp.pixels[i] = (0, 0, max_brightness)
            else:
                print("Invalid entry")
        cp.pixels.show()
        time.sleep(0.3)
        
        quit = input("Would you like to quit? Press q to exit or any other key to continue: ").lower()
        if quit == 'q':
            print("Program ended")
        #Turn off the leds
            for i in range(10):
                cp.pixels[i] = (max_brightness,max_brightness,max_brightness)
                print(f'Turning off Leds {i}')
        #This will break the loop
            max_brightness -= 1 
    except:
        print('Invalid input. Try again')
        
        #Program worked in Thonny using Circuitpy Playground Express
        