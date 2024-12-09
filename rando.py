from sense_hat import SenseHat
import time
import random

def random_color():
    """Generate a random color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def adjust_brightness(color, factor):
    """Adjust the brightness of a color by a given factor."""
    return tuple(max(0, min(255, int(c * factor))) for c in color)

def main():
    sense = SenseHat()
    sense.set_rotation(180)
    
    # Initialize pixel colors and brightness factors
    pixels = [random_color() for _ in range(64)]
    brightness_factors = [random.uniform(0.5, 1.5) for _ in range(64)]
    brightness_directions = [random.choice([-0.01, 0.01]) for _ in range(64)]

    while True:
        for i in range(64):
            # Adjust the brightness factor
            brightness_factors[i] += brightness_directions[i]

            # Reverse direction if the factor goes out of bounds
            if brightness_factors[i] > 1.5 or brightness_factors[i] < 0.5:
                brightness_directions[i] *= -1

            # Calculate the new color with adjusted brightness
            bright_color = adjust_brightness(pixels[i], brightness_factors[i])

            # Set the pixel color
            x, y = divmod(i, 8)
            sense.set_pixel(x, y, bright_color)

        # Small delay to control the update speed
        time.sleep(0.05)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sense = SenseHat()
        sense.clear()
