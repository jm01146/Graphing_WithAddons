# Libraries
import matplotlib.pyplot as plt
import numpy as np

# Sample data for three trials (change these values with your actual data)
trial1 = [50, 80, 36]
trial2 = [96, 57, 79]
trial3 = [10, 88, 79]

# Calculate maximum and average values for each data point
max_values = [max(trial1), max(trial2), max(trial3)]
min_values = [min(trial1), min(trial2), min(trial3)]
average_values = [np.mean(trial1), np.mean(trial2), np.mean(trial3)]

# Number of data points
data_points = len(max_values)
x = np.arange(data_points)

# Bar width
bar_width = 0.35

# Create a figure and two subplots for maximum and average values
fig, ax = plt.subplots()
ax.bar(x, average_values, bar_width, color='green')

# Add lines representing maximum, minimum, in range format
for i in range(data_points):
    ax.plot([x[i] - bar_width / 16, x[i] + bar_width / 16], [max_values[i], max_values[i]], color='black', linewidth=2)
    ax.plot([x[i], x[i]], [max_values[i], min_values[i]], color='black', linewidth=2)
    ax.plot([x[i] - bar_width / 16, x[i] + bar_width / 16], [min_values[i], min_values[i]], color='black', linewidth=2)

# Labels and titles
ax.set_xlabel('(No Triton-x)DBSA concentration (%)')
ax.set_ylabel('sheet resistance (kΩ/▢)')
ax.set_xticks(x)
ax.set_xticklabels(['1.5', '3.0', '4.5'])

# Show the plot
plt.show()
