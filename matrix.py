from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.set_rotation(180)

# Generate green shades ranging from (0, 0, 0) to (0, 255, 0)
colors = [(0, g, 0) for g in range(0, 256, 32)]

def display_matrix_screen():
    columns = 8
    trails = [random.randint(0, 7) for _ in range(columns)]
    # Introduce different delay ranges for each column to vary the speed significantly
    delays = [random.uniform(0.05, 0.5) for _ in range(columns)]

    while True:
        for i in range(columns):
            # Randomly decide if the trail should continue or reset
            if random.random() < 0.1:
                trails[i] = random.randint(0, 7)
            else:
                trails[i] = (trails[i] + 1) % 8
            
            for j in range(8):
                # Calculate the shade based on position
                shade_index = min(j, len(colors) - 1)
                sense.set_pixel(i, (trails[i] + j) % 8, colors[shade_index])

            # Introducing a delay specific to each column to vary the descent speed significantly
            time.sleep(delays[i])

try:
    display_matrix_screen()
except KeyboardInterrupt:
    sense.clear()
