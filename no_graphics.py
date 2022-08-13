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
velb = -1

ms = 1
n = 3
mb = 100**n
dt = 1 / mb * 10**3
counter = 0  # collision counter
run = True

# infinite loop
while run:

    xs += dt * vels
    xb += dt * velb
    # Collision detection
    if xb < 0:
        print("error")
        run = False
    if xb + velb * dt <= 50 + xs + vels * dt:  # Collision of the rectangles
        vels, velb = elastic_col_vel(vels, velb, ms, mb)  # change of vel
        counter += 1
    if xs + vels * dt <= 0:  # Collision of small rectangle with the left wall
        vels = -vels
        counter += 1
    # Ending the simulation when no more collision can occure
    if velb > 0 and vels > 0 and vels < velb:
        run = False


# closes the pygame window and pring digits of pi
digits = [",".join(i) for i in str(counter)]
print("first {} digits of pi are:".format(len(digits)), digits)
