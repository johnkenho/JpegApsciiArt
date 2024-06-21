#Image to ascii art converter
import os
os.chdir('/Users/johnho/Documents/VSC/Python')

from PIL import Image
def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    #Open image and get size
    img = Image.open(image)
    w, h = img.size

    #Resize image
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    #Open resized image
    img = Image.open("resized.%s" % type)
    w, h = img.size #get new image size

    #list with correct length and height
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    #Get pixel data
    pixels = img.load()

    for y in range (h):
        for x in range (w):
            if sum(pixels[x, y]) in range (1,100):
                grid[y][x] = "."
            elif sum(pixels[x, y]) in range (100,200):
                grid[y][x] = "/"
            elif sum(pixels[x, y]) in range (200,300):
                grid[y][x] = "-"
            elif sum(pixels[x, y]) in range (300,400):
                grid[y][x] = "*"
            elif sum(pixels[x, y]) in range (400,500):
                grid[y][x] = "%"
            elif sum(pixels[x, y]) in range (500,600):
                grid[y][x] = "A"
            elif sum(pixels[x, y]) in range (600,700):
                grid[y][x] = "#"

    art = open(saveas, "w")

    for row in grid:  
        art.write("".join(row) + "\n")

    art.close()

if __name__ == "__main__":
    asciiConvert("starrynight.jpeg", "jpeg", "starrynight.txt", "3")




