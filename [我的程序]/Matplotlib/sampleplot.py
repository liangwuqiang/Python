import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.font_manager import FontProperties
cn_font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc')


class MyPlot:

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def set(title=None, x_label=None, y_label=None):
        if title:  # 标题
            plt.title(title, fontproperties=cn_font)
        if x_label:  # x轴
            plt.xlabel(x_label, fontproperties=cn_font)
        if y_label:  # y轴
            plt.ylabel(y_label, fontproperties=cn_font)
        # plt.grid(True)

    @staticmethod
    def plot(x, y, style='g-'):
        plt.plot(x, y, style, linewidth=2)

    @staticmethod
    def hist(x):
        n, bins, patches = plt.hist(x, bins=50, normed=1, facecolor='g', alpha=0.5)
        return n, bins, patches

    @staticmethod
    def bar(data, color, label, width, loc=1):
        n_groups = len(data)
        bar_width = width
        index = np.arange(n_groups) + (loc-1) * bar_width
        error_config = {'ecolor': '0.3'}
        plt.bar(index, data, bar_width, alpha=0.4, color=color, error_kw=error_config, label=label)
        plt.legend()
        pass

    @staticmethod
    def pie(sizes, explode, labels, colors):
        plt.pie(sizes, explode, labels, colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')

    @staticmethod
    def scatter(x, y):
        color = np.arctan2(x, y)
        plt.scatter(x, y, c=color, s=100, alpha=0.6, marker='o')


def plot(my):  # 简单绘图
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)

    my.set(title='简单的图表', x_label='时间 (s)', y_label='电压 (mV)')
    my.plot(t, s)


def subplot(my):  # 子图
    x1 = np.linspace(0, 5)
    x2 = np.linspace(0, 2)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(211)
    my.set(title='具有2子图的图表', y_label='Damped oscillation')
    my.plot(x1, y1, style='yo-')
    plt.subplot(212)
    my.set(x_label='时间 (s)', y_label='Undamped')
    my.plot(x2, y2, style='r.-')


def hist(my):
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(10000)

    my.set(title='IQ的直方图: $\mu=100$, $\sigma=15$', x_label='智力', y_label='概率')
    n, bins, patches = my.hist(x)

    y = mlab.normpdf(bins, mu, sigma)
    my.plot(bins, y, style='r--')


def bar(my):  # 条状图
    first = (20, 35, 30, 35, 27)
    second = (25, 32, 34, 20, 25)

    my.set(title='每组得分情况', x_label='分组', y_label='得分')
    my.bar(first, color='b', label='First', width=0.35, loc=1)
    my.bar(second, color='r', label='Second', width=0.35, loc=2)


def pie(my):
    sizes = [15, 30, 45, 10]
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)
    my.pie(sizes=sizes, labels=labels, colors=colors, explode=explode)


def scatter(my):
    n = 100
    x = np.random.randn(n)
    y = np.random.randn(n)

    my.scatter(x, y)


def fill(my):
    x = np.linspace(0, 1)
    y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

    my.set()
    plt.fill(x, y, 'r')


def main():
    my = MyPlot()

    # plot(my)  # 简单绘图
    # subplot(my)  # 子图
    # hist(my)  # 直方图
    # bar(my)  # 条形图
    # pie(my)  # 饼图
    scatter(my)  # 散点图
    # fill(my)  # 填充曲线

    my.show()
    pass

if __name__ == '__main__':
    main()

