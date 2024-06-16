from django.shortcuts import render
from analysis.classes.chart_creator import ChartCreator
from analysis.classes.population_data_fetcher import PopulationDataFetcher


def growth_rates(request):
    fetcher = PopulationDataFetcher()
    chart_creator = ChartCreator()

    countries, population = fetcher.get_population_data()
    countries1, population1 = fetcher.get_population_growth_data(10)
    countries2, population2 = fetcher.get_population_growth_data(60)

    graphic = chart_creator.create_charts(countries, population, 'Bevolkerungsanzahl', 'Land',
                                          'Top 10 Länder nach Bevölkerungszahl im Jahr 2022')
    graphic1 = chart_creator.create_charts(countries1, population1, 'Wachstumsrate', 'Land',
                                           'Wachstumsrate in den letzten 10 Jahren (2013-2022)')
    graphic2 = chart_creator.create_charts(countries2, population2, 'Wachstumsrate', 'Land',
                                           'Wachstumsrate in den letzten 60 Jahren (1963-2022)')

    return render(request, 'wachstumsraten.html', {'graphic': graphic, 'graphic1': graphic1, 'graphic2': graphic2})


def age_distribution(request):
    fetcher = PopulationDataFetcher()
    chart_creator = ChartCreator()

    years, old_population, middle_population, young_population = fetcher.get_age_distribution_data()
    graphic = chart_creator.create_age_distribution_chart(years, old_population, middle_population, young_population)

    countries_pop_old, population_old = fetcher.get_top_ten_countries_data("old")
    countries_pop_middle, population_middle = fetcher.get_top_ten_countries_data("middle")
    countries_pop_young, population_young = fetcher.get_top_ten_countries_data("young")

    graphic_pop_old = chart_creator.create_charts(countries_pop_old, population_old, 'Bevolkerungsanzahl', 'Land',
                                                  'Top 10 Länder nach Bevölkerungszahl im Alter von 65 Jahren und älter im Jahr 2022')
    graphic_pop_middle = chart_creator.create_charts(countries_pop_middle, population_middle, 'Bevolkerungsanzahl',
                                                     'Land',
                                                     'Top 10 Länder nach Bevölkerungszahl im Alter von 15 bis 64 Jahren im Jahr 2022')
    graphic_pop_young = chart_creator.create_charts(countries_pop_young, population_young, 'Bevolkerungsanzahl', 'Land',
                                                    'Top 10 Länder nach Bevölkerungszahl im Alter bis 14 Jahren im Jahr 2022')

    return render(request, 'altersverteilung.html',
                  {'graphic': graphic, "graphic_old": graphic_pop_old, "graphic_middle": graphic_pop_middle,
                   "graphic_young": graphic_pop_young})


def gender_ratio(request):
    fetcher = PopulationDataFetcher()
    chart_creator = ChartCreator()

    years, male_population, female_population = fetcher.get_gender_ratio_data()
    graphic_world_ratio = chart_creator.create_gender_ratio_chart(years, male_population, female_population)

    countries_male_to_female_percentage, ratios_male_to_female_percentage = fetcher.get_top_countries_by_gender_ratio(
        'male_to_female_percentage')
    graphic_male_to_female_percentage = chart_creator.create_charts(countries_male_to_female_percentage,
                                                                    ratios_male_to_female_percentage,
                                                                    'Anteil der Männer in %', 'Land',
                                                                    'Top 10 Länder nach Verhältnis Männer zu Frauen als Prozentzahl im Jahr 2022',
                                                                    True)

    countries_female_to_male_percentage, ratios_female_to_male_percentage = fetcher.get_top_countries_by_gender_ratio(
        'female_to_male_percentage')
    graphic_female_to_male_percentage = chart_creator.create_charts(countries_female_to_male_percentage,
                                                                    ratios_female_to_male_percentage,
                                                                    'Anteil der Frauen in %', 'Land',
                                                                    'Top 10 Länder nach Verhältnis Frauen zu Männern als Prozentzahl im Jahr 2022',
                                                                    True)

    countries_male, population_male = fetcher.get_top_ten_countries_gender("male")
    countries_female, population_female = fetcher.get_top_ten_countries_gender("female")

    graphic_male = chart_creator.create_charts(countries_male, population_male, 'Bevölkerungsanzahl', 'Land',
                                               'Top 10 Länder nach männlicher Bevölkerungszahl im Jahr 2022')
    graphic_female = chart_creator.create_charts(countries_female, population_female, 'Bevölkerungsanzahl', 'Land',
                                                 'Top 10 Länder nach weiblicher Bevölkerungszahl im Jahr 2022')

    return render(request, 'geschlechterverhaeltnis.html',
                  {'graphic_world_ratio': graphic_world_ratio, 'graphic_male': graphic_male,
                   'graphic_female': graphic_female,
                   'graphic_male_to_female_percentage': graphic_male_to_female_percentage,
                   'graphic_female_to_male_percentage': graphic_female_to_male_percentage})


def home(request):
    return render(request, 'home.html')
