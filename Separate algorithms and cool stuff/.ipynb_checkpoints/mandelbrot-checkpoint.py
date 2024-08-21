from PIL import Image
import colorsys
import math
import os

width = 1000
x = 0
y = 0
xRange = 4
aspectRatio = 4/3 

precision = 250

height = round(width / aspectRatio)
yRange = xRange / aspectRatio
minX = x - xRange / 2
maxX = x + xRange / 2
minY = y - yRange / 2
maxY = y + yRange / 2

img = Image.new('RGB', (width, height), color = 'black')
pixels = img.load()

def logColor(distance, base, const, scale):
    color = -1 * math.log(distance, base)
    rgb = colorsys.hsv_to_rgb(const + scale * color,0.8,0.9)
    return tuple(round(i * 255) for i in rgb)

def powerColor(distance, const, scale):
    color = math.sqrt(distance)
    rgb = colorsys.hsv_to_rgb(const + scale * color, color * 3  + 0.5, distance * 5 + 0.7)
    return tuple(round(i * 255) for i in rgb)

def mapScaleToScale(num, start1, stop1, start2, stop2): 
    return (num - start1) / (stop1 - start1) * (stop2 - start2) + start2

for row in range(height):
    for col in range(width):
        x = mapScaleToScale(col, 0, width, minX, maxX)
        y = mapScaleToScale(row, 0, height, minY, maxY)
        cX = x
        cY = y
        for i in range(precision + 1):
            a = x*x - y*y
            b = 2 * x * y 
            x = a + cX 
            y = b + cY 
            if x*x + y*y > 4:
                break
        if i < precision:
            distance = (i + 1) / (precision + 1)
            rgb = powerColor(distance, 0.65, 0.35)
            pixels[col,row] = rgb

img.save('mandelbrot.png')


