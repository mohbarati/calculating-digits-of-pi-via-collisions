# This code can compute digits of pi via collision without tracking the motion of the objests!
# It only counts the number of times the objects will collide before they never reach eachother.
# Credit for this code goes to: https://github.com/prajwalsouza/ , although mine seems to run faster.
vs = 0
vb = -1
n = 6
ms = 1
mb = 100**n


def elastic_col_vel(v1, v2, m1, m2):
    v1_after = (m1 - m2) / (m1 + m2) * v1 + 2 * m2 / (m1 + m2) * v2
    v2_after = 2 * m1 / (m1 + m2) * v1 - (m1 - m2) / (m1 + m2) * v2
    return v1_after, v2_after


def check_run(v1, v2):
    if v1 < v2 and v1 > 0 and v2 > 0:
        return False
    return True


to_hit = "ball"
counter = 0
while check_run(vs, vb):
    if to_hit == "wall":
        counter += 1
        vs = -vs
        to_hit = "ball"
    else:
        counter += 1
        vs, vb = elastic_col_vel(vs, vb, ms, mb)
        to_hit = "wall"

digits = [",".join(i) for i in str(counter)]
print("The first {} digits of pi are:".format(len(digits)), digits)
