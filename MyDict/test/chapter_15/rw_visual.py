import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
# ## 保证新走,只要程序是活跃的。
while True:
    # Make a random walk, and plot the points.
    # ## 做一个随机游走,情节点。
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    # ## 设置绘图窗口的大小。
    plt.figure(dpi=128, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)
        
    # Emphasize the first and last points.
    # ## 强调第一个和最后一个点。
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)
        
    # Remove the axes.
    # ## 删除轴。
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
        
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
