from django.shortcuts import render
from analysis.models import TotalPopulationData
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from io import BytesIO
import base64


def home(request):
    return render(request, 'home.html')


def growth_rates(request):
    data = TotalPopulationData.objects.filter(country_category='Country').order_by('-year_2022')[:10]
    countries = [entry.country_name for entry in data]
    population = [entry.year_2022/1000000 for entry in data]

    plt.figure(figsize=(9, 6))
    plt.bar(countries, population, color='grey')
    plt.xlabel('Land', color='white')
    plt.ylabel('Bevölkerungsanzahl', color='white')
    plt.title('Top 10 Länder nach Bevölkerungszahl im Jahr 2022', color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    plt.gca().set_facecolor('black')
    plt.gcf().set_facecolor('black')

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

    return render(request, 'wachstumsraten.html', {'graphic': graphic})


def age_distribution(request):
    return render(request, 'altersverteilung.html')


def gender_ratio(request):
    return render(request, 'geschlechterverhaeltnis.html')
