import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# steps of iteration
steps = 10
# projection limits
x_inf, x_sup = -2, 2
y_inf, y_sup = -2, 2
z_inf, z_sup = -2, 2
# starting line
p_0 =  np.array([-2, 0, 1, 1])
p_1 =  np.array([ 2, 2, 1, 1])
# the transformation matrix for each step
theta = np.pi / 2 / steps
trans = np.array([
        [1, 0, 0,  0],
        [0, 1, 0,  -2 / steps],
        [0, 0, 1,  -1 / steps],
        [0, 0, 0,  1]])

###############################################################################

def gen_line(step):
    dims = 3
    points = 2
    # line defined by start and end point
    line_data = np.empty((dims, points))
    tmp_0 = np.copy(p_0)
    tmp_1 = np.copy(p_1)
    # one matrix iteration per step
    for _ in range(step):
        tmp_0 = trans @ tmp_0
        tmp_1 = trans @ tmp_1
    # start
    line_data[:, 0] = tmp_0[:3]
    # end
    line_data[:, 1] = tmp_1[:3]
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
data = [gen_line(i) for i in range(steps)]
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
    fig, update_lines, steps, fargs=(data, lines), interval=500)

line_ani.save("movie.mp4")

plt.show()

