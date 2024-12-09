from sense_hat import SenseHat
import time

sense = SenseHat()

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def color_map(n, max_iter):
    # Cycle between red, green, and blue based on the iteration count
    if n < max_iter:
        r = int(255 * (n / max_iter))
        g = int(255 * ((max_iter - n) / max_iter))
        b = int(255 * ((n / max_iter) ** 0.5))
        return [r, g, b]
    else:
        return [0, 0, 0]  # Black for points in the set

def display_fractal():
    max_iter = 30  # Reduced iterations for faster animation
    while True:
        for posx in range(-4, 4):
            for posy in range(-4, 4):
                re = posx / 4.0
                im = posy / 4.0
                c = complex(re, im)
                n = mandelbrot(c, max_iter)
                color = color_map(n, max_iter)
                sense.set_pixel(posx + 4, posy + 4, color)
        time.sleep(0.05)  # Shorter delay for quicker animation

try:
    display_fractal()
except KeyboardInterrupt:
    sense.clear()
