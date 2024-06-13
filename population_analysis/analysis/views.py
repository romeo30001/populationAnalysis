from django.shortcuts import render
from analysis.models import TotalPopulationData
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from io import BytesIO
from django.db.models import F, ExpressionWrapper, IntegerField
import base64


def home(request):
    return render(request, 'home.html')


def get_population_data():
    data = TotalPopulationData.objects.filter(country_category='Country').order_by('-year_2022')[:10]
    countries = [entry.country_name for entry in data]
    population = [entry.year_2022 / 1000000 for entry in data]
    return countries, population


def get_population_growth_data(years):
    data = TotalPopulationData.objects.filter(country_category='Country')
    data2 = data.annotate(
        population_difference=ExpressionWrapper(
            (F('year_2022') - F('year_2013')) / 1000000, output_field=IntegerField()
        )
    )
    data3 = data.annotate(
        population_difference=ExpressionWrapper(
            (F('year_2022') - F('year_1963')) / 1000000, output_field=IntegerField()
        )
    )
    data2 = data2.order_by('-population_difference')[:10]
    data3 = data3.order_by('-population_difference')[:10]

    if years == 10:
        countries = [entry.country_name for entry in data2]
        population = [entry.population_difference for entry in data2]
    else:
        countries = [entry.country_name for entry in data3]
        population = [entry.population_difference for entry in data3]

    return countries, population


def create_charts(countries, population, ylabel, xlabel, title):
    plt.figure(figsize=(9, 6))
    plt.bar(countries, population, color='#212529')
    plt.xlabel(xlabel, color='black')
    plt.ylabel(ylabel, color='black')
    plt.title(title, color='black')
    plt.xticks(rotation=45, color='black')
    plt.yticks(color='black')
    plt.gca().set_facecolor('#F8F9FA')
    plt.gcf().set_facecolor('#F8F9FA')

    plt.subplots_adjust(top=0.93)
    plt.subplots_adjust(bottom=0.25)

    formatter = FuncFormatter(lambda x, _: f'{int(x)}M')
    plt.gca().yaxis.set_major_formatter(formatter)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')
    return graphic


def growth_rates(request):
    countries, population = get_population_data()
    countries1, population1 = get_population_growth_data(10)
    countries2, population2 = get_population_growth_data(60)
    graphic = create_charts(countries, population, 'Bevolkerungsanzahl', 'Land',
                            'Top 10 Länder nach Bevölkerungszahl im Jahr 2022')
    graphic1 = create_charts(countries1, population1, 'Wachstumsrate', 'Land',
                             'Wachstumsrate in den letzten 10 Jahren (2013-2022)')
    graphic2 = create_charts(countries2, population2, 'Wachstumsrate', 'Land',
                             'Wachstumsrate in den letzten 60 Jahren (1963-2022)')
    return render(request, 'wachstumsraten.html', {'graphic': graphic, 'graphic1': graphic1, 'graphic2': graphic2})


def age_distribution(request):
    return render(request, 'altersverteilung.html')


def gender_ratio(request):
    return render(request, 'geschlechterverhaeltnis.html')
