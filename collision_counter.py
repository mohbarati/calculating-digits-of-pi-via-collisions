# import pygame module in this program
import pygame

pygame.init()
pygame.mixer.init()

# Loading the song
pygame.mixer.music.load("collision_sound.mp3")

# Setting the volume
pygame.mixer.music.set_volume(1)

# create the display surface object
win = pygame.display.set_mode((1000, 500))

# set the pygame window name
pygame.display.set_caption("Colliding rectangles")
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


def elastic_col_vel(v1, v2, m1, m2):
    v1_after = (m1 - m2) / (m1 + m2) * v1 + 2 * m2 / (m1 + m2) * v2
    v2_after = 2 * m1 / (m1 + m2) * v1 - (m1 - m2) / (m1 + m2) * v2
    return v1_after, v2_after


# velocity and time step
vels = 0
velb = -100
dt = 0.001
ms = 1
mb = ms * 10**4

counter = 0  # collision counter
# Indicates pygame is running
run = True

# infinite loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    xs += dt * vels
    xb += dt * velb
    # Collision detection
    if xb + velb * dt <= 50 + xs + vels * dt:  # Collision of the rectangles
        pygame.mixer.music.play()  # Start playing the song
        vels, velb = elastic_col_vel(vels, velb, ms, mb)  # change of vel
        counter += 1
    if xs + vels * dt <= 0:  # Collision of small rectangle with the left wall
        pygame.mixer.music.play()
        vels = -vels
        counter += 1
    # Ending the simulation when no more collision can occure
    if xb > 1000 and velb > vels and vels > 0 and xs > 100:
        run = False
    # completely fill the surface object with black colour
    win.fill((0, 0, 0))

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (xs, ys, widths, heights))
    pygame.draw.rect(win, (255, 255, 0), (xb, yb, widthb, heightb))
    # it refreshes the window
    pygame.display.update()

# closes the pygame window and pring digits of pi
digits = [",".join(i) for i in str(counter)]
print("first {} digits of pi are:".format(len(digits)), digits)
pygame.quit()
