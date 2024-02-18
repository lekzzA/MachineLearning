# Problem -
# Sherif has a car with speed 180 km/h
# Robber has car with speed 150 km/h and 5 minutes head start
# How long does it take to catch the robber?
# Plotting graph of this question.
# 180 km/h = 3 km/min
# 150 km/h = 2.5 km/min
# If robber starts at time t = 0, distance travelled by him (at time t) is d_r = 2.5 * t
# Sherif starts at time t = 5, distance travelled by him (at time t) is d_s = 3 * (t - 5)

import numpy as np
import matplotlib.pyplot as plt

# To get equally spaced sample points between 0 and 40 (will be used for plotting)
t = np.linspace(0, 40, 100)

# Distance travelled by robber at t
d_r = 2.5 * t

# Distance travelled by sherif at t
d_s = 3 * (t-5)

# Instance of figure (fig) and array of axes (ax)
# Parameter 1 -> number of rows in subplot
# Parameter 2 -> number of columns in subplot.
fig, ax = plt.subplots(1, 3)

# Plotting robber on first subplot
ax[0].plot(t, d_r, c="green")
ax[0].set_title("Robber")

# Calculating slope of line.
slope_r = (d_r[10] - d_r[0]) / (t[10] - t[0])
# Converting to radian
angle_rad_r = np.arctan(slope_r)

# Writing slope on the line rotated by angle of slope.
ax[0].text(t[10], d_r[10]+15, f'Slope = {slope_r:.2f}', rotation=np.degrees(angle_rad_r))

# Plotting sherif on second subplot similar to first one.
ax[1].plot(t, d_s, c="red")
ax[1].set_title("Sherif")
slope_s = (d_s[10] - d_s[0]) / (t[10] - t[0])
angle_rad_s = np.arctan(slope_s)
ax[1].text(t[20], d_s[20]+15, f'Slope = {slope_s:.2f}', rotation=np.degrees(angle_rad_s))

# Plotting both together on third subplot
ax[2].plot(t, d_r, c="green")
ax[2].plot(t, d_s, c="red")

# Setting axes names, scale of axes, vertical and horizontal lines.
for axes in ax:
    axes.set_xlabel("time (in minutes)")
    axes.set_ylabel("distance (in km)")
    axes.set_xlim([0, 40])
    axes.set_ylim([0, 100])
    axes.axvline(x=30, c="purple", linestyle="--")
    axes.axhline(y=75, c="purple", linestyle="--")

# Showing the plots.
plt.show()
