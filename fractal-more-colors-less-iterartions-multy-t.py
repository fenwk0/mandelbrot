from sense_hat import SenseHat
import time
import concurrent.futures

sense = SenseHat()
sense.set_rotation(180)

# Constants
MAX_ITER = 30
THREAD_COUNT = 4  # Number of threads (typically match this to the number of cores)

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def color_map(n, max_iter):
    if n < max_iter:
        r = int(255 * (n / max_iter))
        g = int(255 * ((max_iter - n) / max_iter))
        b = int(255 * ((n / max_iter) ** 0.5))
        return [r, g, b]
    else:
        return [0, 0, 0]

def calculate_and_display(start, end):
    for posx in range(start, end):
        for posy in range(-4, 4):
            re = posx / 4.0
            im = posy / 4.0
            c = complex(re, im)
            n = mandelbrot(c, MAX_ITER)
            color = color_map(n, MAX_ITER)
            sense.set_pixel(posx + 4, posy + 4, color)

def display_fractal():
    ranges = [(-4, -2), (-2, 0), (0, 2), (2, 4)]
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
            # Divide the work among threads
            executor.map(lambda r: calculate_and_display(*r), ranges)
        time.sleep(0.05)

try:
    display_fractal()
except KeyboardInterrupt:
    sense.clear()
