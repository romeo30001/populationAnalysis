from django.shortcuts import render
from analysis.models import TotalPopulationData, MalePopulationData, FemalePopulationData, OldAgeData, MiddleAgeData, \
    YoungAgeData
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from io import BytesIO
from django.db.models import F, ExpressionWrapper, IntegerField
import base64


def get_age_distribution_data():
    old_age_data = OldAgeData.objects.filter(country_name='World').first()
    middle_age_data = MiddleAgeData.objects.filter(country_name='World').first()
    young_age_data = YoungAgeData.objects.filter(country_name='World').first()

    years = list(range(1967, 2023, 5))
    old_population = [getattr(old_age_data, f'year_{year}') for year in years]
    middle_population = [getattr(middle_age_data, f'year_{year}') for year in years]
    young_population = [getattr(young_age_data, f'year_{year}') for year in years]

    return years, old_population, middle_population, young_population


def get_top_ten_countries_data(category):
    old_age_data = OldAgeData.objects.filter(country_category='Country').order_by('-year_2022')[:10]
    middle_age_data = MiddleAgeData.objects.filter(country_category='Country').order_by('-year_2022')[:10]
    young_age_data = YoungAgeData.objects.filter(country_category='Country').order_by('-year_2022')[:10]

    old_countries = [data.country_name for data in old_age_data]
    old_population = [data.year_2022 / 1000000 for data in old_age_data]
    middle_countries = [data.country_name for data in middle_age_data]
    middle_population = [data.year_2022 / 1000000 for data in middle_age_data]
    young_countries = [data.country_name for data in young_age_data]
    young_population = [data.year_2022 / 1000000 for data in young_age_data]

    if category == "old":
        return old_countries, old_population
    elif category == "middle":
        return middle_countries, middle_population
    else:
        return young_countries, young_population


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
        formatter = FuncFormatter(lambda x, _: f'{x:.2f}' if 'Verhältnis' in ylabel else f'{int(x)}')
        plt.gca().yaxis.set_major_formatter(formatter)

        for bar, value in zip(bars, population):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                     f'{value:.2f}' if 'Verhältnis' in ylabel else f'{value:.0f}',
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


def get_gender_ratio_data():
    male_data = MalePopulationData.objects.filter(country_name='World').first()
    female_data = FemalePopulationData.objects.filter(country_name='World').first()

    years = list(range(1967, 2023, 5))
    male_population = [getattr(male_data, f'year_{year}') for year in years]
    female_population = [getattr(female_data, f'year_{year}') for year in years]

    return years, male_population, female_population


def get_top_ten_countries_gender(category):
    male_data = MalePopulationData.objects.filter(country_category='Country').order_by('-year_2022')[:10]
    female_data = FemalePopulationData.objects.filter(country_category='Country').order_by('-year_2022')[:10]

    male_countries = [data.country_name for data in male_data]
    male_population = [data.year_2022 / 1000000 for data in male_data]
    female_countries = [data.country_name for data in female_data]
    female_population = [data.year_2022 / 1000000 for data in female_data]

    if category == "male":
        return male_countries, male_population
    else:
        return female_countries, female_population


def get_top_countries_by_gender_ratio(ratio_type):
    male_data = MalePopulationData.objects.filter(country_category='Country')
    female_data = FemalePopulationData.objects.filter(country_category='Country')

    ratios = []
    if ratio_type == 'male_to_female':
        for male, female in zip(male_data, female_data):
            ratio = male.year_2022 / female.year_2022 if female.year_2022 != 0 else 0
            ratios.append((male.country_name, ratio))
        ratios = sorted(ratios, key=lambda x: x[1], reverse=True)[:10]
    elif ratio_type == 'female_to_male':
        for male, female in zip(male_data, female_data):
            ratio = female.year_2022 / male.year_2022 if male.year_2022 != 0 else 0
            ratios.append((female.country_name, ratio))
        ratios = sorted(ratios, key=lambda x: x[1], reverse=True)[:10]

    countries = [x[0] for x in ratios]
    values = [x[1] for x in ratios]
    return countries, values


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
    years, old_population, middle_population, young_population = get_age_distribution_data()
    graphic = create_age_distribution_chart(years, old_population, middle_population, young_population)
    countries_pop_old, population_old = get_top_ten_countries_data("old")
    countries_pop_middle, population_middle = get_top_ten_countries_data("middle")
    countries_pop_young, population_young = get_top_ten_countries_data("young")

    graphic_pop_old = create_charts(countries_pop_old, population_old, 'Bevolkerungsanzahl', 'Land',
                                    'Top 10 Länder nach Bevölkerungszahl im Alter von 65 Jahren und älter im Jahr 2022')
    graphic_pop_middle = create_charts(countries_pop_middle, population_middle, 'Bevolkerungsanzahl', 'Land',
                                       'Top 10 Länder nach Bevölkerungszahl im Alter von 15 bis 64 Jahren im Jahr 2022')
    graphic_pop_young = create_charts(countries_pop_young, population_young, 'Bevolkerungsanzahl', 'Land',
                                      'Top 10 Länder nach Bevölkerungszahl im Alter bis 14 Jahren im Jahr 2022')
    return render(request, 'altersverteilung.html',
                  {'graphic': graphic, "graphic_old": graphic_pop_old, "graphic_middle": graphic_pop_middle,
                   "graphic_young": graphic_pop_young})


def gender_ratio(request):
    years, male_population, female_population = get_gender_ratio_data()
    graphic_world_ratio = create_gender_ratio_chart(years, male_population, female_population)

    countries_male_to_female, ratios_male_to_female = get_top_countries_by_gender_ratio('male_to_female')
    countries_female_to_male, ratios_female_to_male = get_top_countries_by_gender_ratio('female_to_male')

    graphic_male_to_female = create_charts(
        countries_male_to_female, ratios_male_to_female, 'Verhältnis', 'Land',
        'Top 10 Länder nach Verhältnis Männer zu Frauen im Jahr 2022', True
    )
    graphic_female_to_male = create_charts(
        countries_female_to_male, ratios_female_to_male, 'Verhältnis', 'Land',
        'Top 10 Länder nach Verhältnis Frauen zu Männern im Jahr 2022', True
    )

    countries_male, population_male = get_top_ten_countries_gender("male")
    countries_female, population_female = get_top_ten_countries_gender("female")

    graphic_male = create_charts(countries_male, population_male, 'Bevölkerungsanzahl', 'Land',
                                 'Top 10 Länder nach männlicher Bevölkerungszahl im Jahr 2022')
    graphic_female = create_charts(countries_female, population_female, 'Bevölkerungsanzahl', 'Land',
                                   'Top 10 Länder nach weiblicher Bevölkerungszahl im Jahr 2022')

    return render(request, 'geschlechterverhaeltnis.html',
                  {'graphic_world_ratio': graphic_world_ratio,
                   'graphic_male': graphic_male,
                   'graphic_female': graphic_female,
                   'graphic_male_to_female': graphic_male_to_female,
                   'graphic_female_to_male': graphic_female_to_male})


def home(request):
    return render(request, 'home.html')
