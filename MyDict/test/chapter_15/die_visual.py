import pygal

from die import Die

# Create a D6.
# ## 创建一个D6。
die = Die()

# Make some rolls, and store results in a list.
# ## 做一些卷,并将结果存储在一个列表。
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results.
# ## 分析结果。
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
# ## 可视化结果。
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
