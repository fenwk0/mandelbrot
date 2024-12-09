from sense_hat import SenseHat
import time
import math

sense = SenseHat()

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def color_map(n, max_iter):
    return [int(255 * (n / max_iter)), int(255 * ((n / max_iter) ** 0.5)), 0]

def display_fractal():
    max_iter = 50
    while True:
        for posx in range(-4, 4):
            for posy in range(-4, 4):
                re = posx / 4.0
                im = posy / 4.0
                c = complex(re, im)
                n = mandelbrot(c, max_iter)
                color = color_map(n, max_iter)
                sense.set_pixel(posx + 4, posy + 4, color)
        time.sleep(0.1)  # Delay to slow down the animation

try:
    display_fractal()
except KeyboardInterrupt:
    sense.clear()
