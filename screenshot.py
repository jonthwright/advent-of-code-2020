import pyscreenshot as ImageGrab

upper = 185
im = ImageGrab.grab(bbox=(0, upper, 650, upper + 600))
im.save('map.png')