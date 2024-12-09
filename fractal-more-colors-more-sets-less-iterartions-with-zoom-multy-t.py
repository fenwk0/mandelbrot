from sense_hat import SenseHat
import time
import concurrent.futures
import random

sense = SenseHat()
sense.set_rotation(180)

# Constants
MAX_ITER = 30
THREAD_COUNT = 4
ZOOM_FACTOR = 0.998  # Increment the zoom effect per iteration

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def julia(z, c, max_iter):
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def burning_ship(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = complex(abs(z.real), abs(z.imag))
        z = z*z + c
        n += 1
    return n

def tricorn(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = complex(z.real, -z.imag)
        z = z*z + c
        n += 1
    return n

def custom_fractal_1(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z*z + c  # Cubic Mandelbrot variant
        n += 1
    return n

def custom_fractal_2(c, max_iter):
    z = complex(random.uniform(-1, 1), random.uniform(-1, 1))
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + complex(z.real**2, -z.imag**2) + c  # A complex transformation
        n += 1
    return n

def color_map(n, max_iter):
    if n < max_iter:
        return [int(255 * (n / max_iter)), int(255 * ((max_iter - n) / max_iter)), int(255 * ((n / max_iter) ** 0.5))]
    else:
        return [0, 0, 0]

def calculate_and_display(start, end, fractal_type, param, boundary):
    for posx in range(start, end):
        for posy in range(-4, 4):
            re = boundary[0] + (posx / 8) * (boundary[1] - boundary[0])
            im = boundary[2] + (posy / 8) * (boundary[3] - boundary[2])
            point = complex(re, im)
            
            if fractal_type == 'mandelbrot':
                n = mandelbrot(point, MAX_ITER)
            elif fractal_type == 'julia':
                n = julia(point, param, MAX_ITER)
            elif fractal_type == 'burning_ship':
                n = burning_ship(point, MAX_ITER)
            elif fractal_type == 'tricorn':
                n = tricorn(point, MAX_ITER)
            elif fractal_type == 'custom_1':
                n = custom_fractal_1(point, MAX_ITER)
            elif fractal_type == 'custom_2':
                n = custom_fractal_2(point, MAX_ITER)
            else:
                n = mandelbrot(point, MAX_ITER)  # Default to mandelbrot
            
            color = color_map(n, MAX_ITER)
            sense.set_pixel(posx + 4, posy + 4, color)

def display_fractal():
    ranges = [(-4, -2), (-2, 0), (0, 2), (2, 4)]
    fractal_types = ['mandelbrot', 'julia', 'burning_ship', 'tricorn', 'custom_1', 'custom_2']
    initial_boundary = [-2.0, 2.0, -2.0, 2.0]  # Start with a wide view

    for _ in range(100):  # Cycle through 100 fractals
        fractal_type = random.choice(fractal_types)
        param = complex(random.uniform(-1, 1), random.uniform(-1, 1)) if fractal_type == 'julia' else None
        boundary = initial_boundary[:]
        
        for _ in range(1000):  # Zoom 1000 times per fractal
            with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
                executor.map(lambda r: calculate_and_display(*r, fractal_type, param, boundary), ranges)
            
            # Zoom in
            center_x = (boundary[0] + boundary[1]) / 2
            center_y = (boundary[2] + boundary[3]) / 2
            width = (boundary[1] - boundary[0]) * ZOOM_FACTOR
            height = (boundary[3] - boundary[2]) * ZOOM_FACTOR
            
            boundary = [
                center_x - width / 2,
                center_x + width / 2,
                center_y - height / 2,
                center_y + height / 2
            ]
            
            time.sleep(0.01)  # Short delay for smoother transitions

try:
    display_fractal()
except KeyboardInterrupt:
    sense.clear()
