#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import cos, sin, pi

###############################################################################
# Line Translation

"""
# steps of iteration
steps = 10
# projection limits
x_inf, x_sup = -2, 3
y_inf, y_sup = -2, 3
z_inf, z_sup = -2, 3
# starting lines
line = [
    [-2, 0, 1],
    [3, 2, 1]
    ]
# the transformation matrix for each step
trans = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, -2 / steps],
        [0, 0, 1, -1 / steps],
        [0, 0, 0, 1]])
"""

###############################################################################
# Triangle Rotation

"""
# steps of iteration
steps = 10
# projection limits
x_inf, x_sup = -1.5, 1.5
y_inf, y_sup = -1.5, 1.5
z_inf, z_sup = -1.5, 1.5
# starting lines
line = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 1],
    [1, 0, 0]
    ]
# the transformation matrix for each step
theta = pi / 2 / steps
trans = np.array([
        [1, 0,           0,          0],
        [0, cos(theta), -sin(theta), 0],
        [0, sin(theta),  cos(theta), 0],
        [0, 0,           0,          1]])
"""

###############################################################################
# Rectangle Rotation

# steps of iteration
steps = 10
# projection limits
x_inf, x_sup = -1.5, 1.5
y_inf, y_sup = -1.5, 1.5
z_inf, z_sup = -1.5, 1.5
# starting lines
line = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
    ]
# the transformation matrix for each step
theta = pi / steps
trans = np.array([
        [1, 0,           0,          0],
        [0, cos(theta), -sin(theta), 0],
        [0, sin(theta),  cos(theta), 0],
        [0, 0,           0,          1]])

###############################################################################


def gen_line(step):
    dims = 3
    points = len (line)
    # line defined by start and end point
    line_data = np.empty((dims, points))
    for i in range(points):
        tmp = np.array(line[i] + [1])
        # one matrix iteration per step
        for _ in range(step):
            tmp = trans @ tmp
        line_data[:, i] = tmp[:3]
    return line_data

def update_lines(num, data_lines, lines):
    for i in range(num):
        line = lines[i]
        data = data_lines[i]
        line.set_data(data[0:2, :])
        line.set_3d_properties(data[2, :])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# one line for each step
data = [gen_line(i) for i in range(steps+1)]
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([x_inf, x_sup])
ax.set_xlabel('X')
ax.set_ylim3d([y_inf, y_sup])
ax.set_ylabel('Y')
ax.set_zlim3d([z_inf, z_sup])
ax.set_zlabel('Z')
ax.set_title('Transformaciones')

# Creating the Animation object
line_ani = animation.FuncAnimation(
    fig, update_lines, steps+2, fargs=(data, lines), interval=250)

#line_ani.save("movie.mp4")

plt.show()

