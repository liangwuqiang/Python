import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=0, show_legend=False)

chart.title = 'Python 项目'
chart.x_labels = ['httpie命令行', '网页django', '中文flask']

plot_dicts = [
    {'value': 16101, 'label': 'httpie的描述.'},
    {'value': 15028, 'label': 'django的描述.'},
    {'value': 4798, 'label': 'flask的描述.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
