#LC101Blurring.py


from image import cImage
import sys
import random

img = image.Image("lcastle.jpg", '')
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # TODO: Randomly choose the coordinates of a neighboring pixel
        x = random.randrange(1, 3)
        y = random.randrange(1, 3)

        if x == 1:
            xadjustment = -1
        else:
            xadjustment = 1

        if y == 1:
            yadjustment = -1
        else:
            yadjustment = 1

        randPixel = img.getPixel(i + xadjustment, j + yadjustment)
        # TODO: in the new image, set this pixel's color to the neighbor's color
        newimg.setPixel(i, j, randPixel)

# buy ourselves some time
#sys.getExecutionLimit(80000) # If you are getting "timeout" errors, increase the 30000

newimg.draw(win)
win.exitonclick()
