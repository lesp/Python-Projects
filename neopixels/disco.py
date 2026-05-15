import machine
import neopixel
import random
import time

np = neopixel.NeoPixel(machine.Pin(7), 1)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    np[0] = (r, g, b)
    np.write()
    time.sleep(0.5)