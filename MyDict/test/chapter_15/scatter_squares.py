import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# Set chart title, and label axes.
# ## 设置图表标题、标签和轴。
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
# ## 设置标记标签的大小。
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
# ## 设置每个轴的范围。
plt.axis([0, 1100, 0, 1100000])

plt.show()
