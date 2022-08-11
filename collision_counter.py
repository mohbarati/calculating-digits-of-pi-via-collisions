# import pygame module in this program
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((1000, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")
# dimensions of the object
widths = 50
heights = 50
widthb = 200
heightb = 200
# object current co-ordinates
xs = 200
ys = 500 - heights
xb = 500
yb = 500 - heightb

# velocity and time step
vels = -10
velb = -5
dt = 0.01
mb = 100
ms = 10
counter = 0
# Indicates pygame is running
run = True

# infinite loop
while run:

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if xb + velb * dt <= 50 + xs + vels * dt:
        counter += 1

    if xs + vel * dt <= 0:
        vel = -vel
        counter += 1
    # completely fill the surface object with black colour
    win.fill((0, 0, 0))

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (xs, ys, widths, heights))
    pygame.draw.rect(win, (255, 255, 0), (xb, yb, widthb, heightb))
    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
