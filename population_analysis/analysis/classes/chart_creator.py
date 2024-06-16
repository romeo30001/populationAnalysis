import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from io import BytesIO
import base64
matplotlib.use('Agg')


class ChartCreator:
    """
    A class to create and render charts.
    """

    @staticmethod
    def create_age_distribution_chart(years, old_population, middle_population, young_population):
        plt.figure(figsize=(8.75, 7))

        plt.plot(years, old_population, marker='o', linestyle='-', color='#212529', label='Alte (65+)')
        plt.plot(years, middle_population, marker='s', linestyle='-', color='#212529', label='Mittlere (15-64)')
        plt.plot(years, young_population, marker='^', linestyle='-', color='#212529', label='Junge (bis 14)')

        plt.xlabel('Jahr', color='black')
        plt.ylabel('Bevölkerungsanzahl', color='black')
        plt.title('Altersverteilung der Bevölkerung', color='black')

        plt.xticks(years, rotation=45, color='black')
        plt.yticks(color='black')

        plt.legend()

        plt.gca().set_facecolor('#F8F9FA')
        plt.gcf().set_facecolor('#F8F9FA')

        plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))

        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x / 1000000000)}Mrd.'))

        plt.subplots_adjust(top=0.92)
        plt.subplots_adjust(bottom=0.25)
        plt.subplots_adjust(left=0.085)
        plt.subplots_adjust(right=0.999)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic

    @staticmethod
    def create_charts(countries, population, ylabel, xlabel, title, ratio=False):
        plt.figure(figsize=(8.75, 7))
        bars = plt.bar(countries, population, color='#212529')
        plt.xlabel(xlabel, color='black')
        plt.ylabel(ylabel, color='black')
        plt.title(title, color='black')
        plt.xticks(rotation=45, color='black')
        plt.yticks(color='black')
        plt.gca().set_facecolor('#F8F9FA')
        plt.gcf().set_facecolor('#F8F9FA')

        plt.subplots_adjust(top=0.93)
        plt.subplots_adjust(bottom=0.25)
        plt.subplots_adjust(left=0.088)
        plt.subplots_adjust(right=0.999)

        if ratio:
            formatter = FuncFormatter(lambda x, _: f'{int(x)}%')
            plt.gca().yaxis.set_major_formatter(formatter)

            for bar, value in zip(bars, population):
                plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                         f'{value:.2f}%' if 'Verhältnis' in ylabel else f'{value:.0f}%',
                         ha='center', va='bottom', color='black')

            max_y_value = max(population)
            plt.gca().set_ylim(0, max_y_value * 1.15)

        else:
            formatter = FuncFormatter(lambda x, _: f'{int(x)}M')
            plt.gca().yaxis.set_major_formatter(formatter)

            for bar, value in zip(bars, population):
                plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                         f'{value:.0f}M', ha='center', va='bottom', color='black')

            max_y_value = max(population)
            plt.gca().set_ylim(0, max_y_value * 1.15)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic

    @staticmethod
    def create_gender_ratio_chart(years, male_population, female_population):
        plt.figure(figsize=(8.75, 7))

        plt.plot(years, male_population, marker='o', linestyle='-', color='#212529', label='Männlich')
        plt.plot(years, female_population, marker='s', linestyle='-', color='#212529', label='Weiblich')

        plt.xlabel('Jahr', color='black')
        plt.ylabel('Bevölkerungsanzahl', color='black')
        plt.title('Geschlechterverhältnis der Weltbevölkerung', color='black')

        plt.xticks(years, rotation=45, color='black')
        plt.yticks(color='black')

        plt.legend()

        plt.gca().set_facecolor('#F8F9FA')
        plt.gcf().set_facecolor('#F8F9FA')

        plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))

        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x / 1000000000)}Mrd.'))

        plt.subplots_adjust(top=0.92)
        plt.subplots_adjust(bottom=0.25)
        plt.subplots_adjust(left=0.085)
        plt.subplots_adjust(right=0.999)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic