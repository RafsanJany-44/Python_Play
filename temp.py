
from images import Image

def colorFilter(image, rgbTriple):
    for j in range(image.getHeight()):
        for i in range(image.getWidth()):
            image.setPixel(i, j, adjust_pixel(image.getPixel(i, j), rgbTriple))


def adjust_pixel(pixel, rgb_adjustment):
    colors = list(pixel)
    adjustment = list(rgb_adjustment)
    for rgb in range(3):
        colors[rgb] += adjustment[rgb]
        if colors[rgb] < 0:
            colors[rgb] = 0
        elif colors[rgb] > 255:
            colors[rgb] = 255
    return tuple(colors)


def lighten(image, amount):
    rgb_adjustment = (amount, amount, amount)
    colorFilter(image, rgb_adjustment)


def darken(image, amount):
    rgb_adjustment = (-amount, -amount, -amount)
    colorFilter(image, rgb_adjustment)


def main():
    file_input = input("Enter the image file name: ")
    image = Image(file_input)
    lighten(image, 128) 
    image.draw()


if __name__ == "__main__":
    main()