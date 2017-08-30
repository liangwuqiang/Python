import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=0, show_legend=False)

chart.title = 'Python 工程'
chart.x_labels = ['http', 'djgo', 'flk']

plot_dicts = [
    {'value': 16101, 'label': 'httpie命令行访问网页.'},
    {'value': 5028, 'label': 'django网页框架.'},
    {'value': 14798, 'label': 'flask轻量级网页框架.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
