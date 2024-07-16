import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from io import BytesIO
import base64

matplotlib.use('Agg')


class ChartCreator:
    """
    A class to create charts.
    """

    def __init__(self, figsize=(8.75, 7), facecolor='#F8F9FA', legend_location='best'):
        """
        :param figsize: Size of the figure.
        :param facecolor: Background color of the chart.
        :param legend_location: Location of the legend.
        """
        self.figsize = figsize
        self.facecolor = facecolor
        self.legend_location = legend_location

    def _apply_common_formatting(self, xlabel, ylabel, title):
        """
        Apply common formatting to the chart.

        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param title: Title of the chart.
        """
        plt.xlabel(xlabel, color='black')
        plt.ylabel(ylabel, color='black')
        plt.title(title, color='black')
        plt.xticks(rotation=45, color='black')
        plt.yticks(color='black')
        plt.gca().set_facecolor(self.facecolor)
        plt.gcf().set_facecolor(self.facecolor)
        plt.subplots_adjust(top=0.97, left=0.087, right=0.999)

    @staticmethod
    def _save_and_encode():
        """
        Save the chart to a buffer and encode it in base64.

        :return: Base64 encoded string of the chart image.
        """
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        return base64.b64encode(image_png).decode('utf-8')

    def create_bar_chart(self, categories, values, ylabel, xlabel, title, ratio=False, space_too_long=False,
                         space_too_small=False):
        """
        Creates a bar chart.

        :param categories: List of categories for the x-axis.
        :param values: List of values for the y-axis.
        :param ylabel: Label for the y-axis.
        :param xlabel: Label for the x-axis.
        :param title: Title of the chart.
        :param ratio: Boolean indicating if the y-axis should be formatted as a percentage.
        :param space_too_long: Boolean indicating if the bottom space should be adjusted for long labels.
        :param space_too_small: Boolean indicating if the bottom space should be adjusted for short labels.
        :return: Base64 encoded string of the bar chart image.
        """

        plt.figure(figsize=self.figsize)
        bars = plt.bar(categories, values, color='#212529')

        self._apply_common_formatting(xlabel, ylabel, title)

        if space_too_long:
            plt.subplots_adjust(bottom=0.15)
        elif space_too_small:
            plt.subplots_adjust(bottom=0.21)
        else:
            plt.subplots_adjust(bottom=0.19)

        if ratio:
            formatter = FuncFormatter(lambda x, _: f'{int(x)}%')
            plt.gca().yaxis.set_major_formatter(formatter)
            for bar, value in zip(bars, values):
                plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{value:.2f}%', ha='center',
                         va='bottom', color='black')
        else:
            formatter = FuncFormatter(lambda x, _: f'{int(x)}M')
            plt.gca().yaxis.set_major_formatter(formatter)
            for bar, value in zip(bars, values):
                plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{value:.0f}M', ha='center',
                         va='bottom', color='black')

        max_y_value = max(values)
        plt.gca().set_ylim(0, max_y_value * 1.15)

        return self._save_and_encode()

    def create_line_chart(self, years, data_series, labels, xlabel, ylabel, title, y_format='Mrd.'):
        """
        Creates a line chart with multiple data series.

        :param years: List of years.
        :param data_series: List of lists, where each sublist contains data points for a series.
        :param labels: List of labels for the data series.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param title: Title of the chart.
        :param y_format: Format for y-axis labels. Default is 'Mrd.' (billions).
        :return: Base64 encoded string of the line chart image.
        """
        plt.figure(figsize=self.figsize)

        # Define markers and colors
        markers = ['o', 's', '^']
        colors = ['#212529']

        for i, (data, label) in enumerate(zip(data_series, labels)):
            plt.plot(years, data, marker=markers[i % len(markers)], linestyle='-', color=colors[i % len(colors)],
                     label=label)

        self._apply_common_formatting(xlabel, ylabel, title)

        plt.legend(loc=self.legend_location)
        plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))
        if y_format == 'Mrd.':
            plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x / 1000000000)}Mrd.'))
        elif y_format == 'M':
            plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x / 1000000)}M'))

        plt.subplots_adjust(bottom=0.099)

        return self._save_and_encode()
