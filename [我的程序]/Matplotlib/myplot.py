import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
cn_font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc')


class MyPlot:
    def __init__(self, x, y, style='g-', title=None, x_label=None, y_label=None):
        self.x = x
        self.y = y
        self.style = style
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def plot(self):
        plt.plot(self.x, self.y, self.style, lw=2)
        if self.title:
            plt.title(self.title, fontproperties=cn_font)
        if self.x_label:
            plt.xlabel(self.x_label, fontproperties=cn_font)
        if self.y_label:
            plt.ylabel(self.y_label, fontproperties=cn_font)
        # plt.grid(True)

    @staticmethod
    def show():
        plt.show()


def main():
    import numpy as np
    x1 = np.linspace(0, 5)
    x2 = np.linspace(0, 2)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(211)
    my = MyPlot(x1, y1, style='yo-', title='A table of 2 subplots', y_label='Damped oscillation')
    my.plot()
    plt.subplot(212)
    my = MyPlot(x2, y2, style='r.-', x_label='time (s)', y_label='Undamped')
    my.plot()

    my.show()


if __name__ == '__main__':
    main()

