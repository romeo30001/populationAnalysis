from django.shortcuts import render
from analysis.classes.chart_creator import ChartCreator
from analysis.classes.population_data_fetcher import PopulationDataFetcher

fetcher = PopulationDataFetcher()
chart_creator = ChartCreator()


def growth_rates(request):
    """
    Renders the 'wachstumsraten.html' template with population growth data and charts.
    """
    top_countries, top_population = fetcher.get_population_data()
    growth_countries_10, growth_population_10 = fetcher.get_population_growth_data(10)
    growth_countries_60, growth_population_60 = fetcher.get_population_growth_data(60)

    population_chart = chart_creator.create_bar_chart(top_countries, top_population, 'Bevolkerungsanzahl', 'Land',
                                                      'Top 10 Länder nach Bevölkerungszahl im Jahr 2022')
    growth_chart_10_years = chart_creator.create_bar_chart(growth_countries_10, growth_population_10, 'Wachstumsrate',
                                                           'Land',
                                                           'Wachstumsrate in den letzten 10 Jahren (2013-2022)')
    growth_chart_60_years = chart_creator.create_bar_chart(growth_countries_60, growth_population_60, 'Wachstumsrate',
                                                           'Land',
                                                           'Wachstumsrate in den letzten 60 Jahren (1963-2022)', False,
                                                           True)

    return render(request, 'wachstumsraten.html',
                  {'population_chart': population_chart, 'growth_chart_10_years': growth_chart_10_years,
                   'growth_chart_60_years': growth_chart_60_years})


def age_distribution(request):
    """
    Renders the 'altersverteilung.html' template with age distribution data and charts.
    """

    years, old_population, middle_population, young_population = fetcher.get_age_distribution_data()
    age_distribution_chart = chart_creator.create_line_chart(years,
                                                             [old_population, middle_population, young_population],
                                                             ['Alte (65+)', 'Mittlere (15-64)', 'Junge (bis 14)'],
                                                             'Jahr',
                                                             'Bevölkerungsanzahl', 'Altersverteilung der Bevölkerung')

    countries_pop_old, population_old = fetcher.get_top_ten_countries_data("old")
    countries_pop_middle, population_middle = fetcher.get_top_ten_countries_data("middle")
    countries_pop_young, population_young = fetcher.get_top_ten_countries_data("young")

    chart_pop_old = chart_creator.create_bar_chart(countries_pop_old, population_old, 'Bevolkerungsanzahl', 'Land',
                                                   'Top 10 Länder nach Bevölkerungszahl im Alter von 65 Jahren und älter im Jahr 2022')
    chart_pop_middle = chart_creator.create_bar_chart(countries_pop_middle, population_middle, 'Bevolkerungsanzahl',
                                                      'Land',
                                                      'Top 10 Länder nach Bevölkerungszahl im Alter von 15 bis 64 Jahren im Jahr 2022')
    chart_pop_young = chart_creator.create_bar_chart(countries_pop_young, population_young, 'Bevolkerungsanzahl',
                                                     'Land',
                                                     'Top 10 Länder nach Bevölkerungszahl im Alter bis 14 Jahren im Jahr 2022')

    return render(request, 'altersverteilung.html',
                  {'age_distribution_chart': age_distribution_chart, "chart_old": chart_pop_old,
                   "chart_middle": chart_pop_middle,
                   "chart_young": chart_pop_young})


def gender_ratio(request):
    """
    Renders the 'geschlechterverhaeltnis.html' template with gender ratio data and charts.
    """

    years, male_population, female_population = fetcher.get_gender_ratio_data()
    chart_world_ratio = chart_creator.create_line_chart(years, [male_population, female_population],
                                                        ['Männlich', 'Weiblich'], 'Jahr', 'Bevölkerungsanzahl',
                                                        'Geschlechterverhältnis der Weltbevölkerung')

    countries_male_to_female_percentage, ratios_male_to_female_percentage = fetcher.get_top_countries_by_gender_ratio(
        'male_to_female_percentage')
    chart_male_to_female_percentage = chart_creator.create_bar_chart(countries_male_to_female_percentage,
                                                                     ratios_male_to_female_percentage,
                                                                     'Anteil der Männer in %', 'Land',
                                                                     'Top 10 Länder nach Verhältnis Männer zu Frauen im Jahr 2022',
                                                                     True, False, True)

    countries_female_to_male_percentage, ratios_female_to_male_percentage = fetcher.get_top_countries_by_gender_ratio(
        'female_to_male_percentage')
    chart_female_to_male_percentage = chart_creator.create_bar_chart(countries_female_to_male_percentage,
                                                                     ratios_female_to_male_percentage,
                                                                     'Anteil der Frauen in %', 'Land',
                                                                     'Top 10 Länder nach Verhältnis Frauen zu Männern im Jahr 2022',
                                                                     True)

    countries_male, population_male = fetcher.get_top_ten_countries_gender("male")
    countries_female, population_female = fetcher.get_top_ten_countries_gender("female")

    chart_male = chart_creator.create_bar_chart(countries_male, population_male, 'Bevölkerungsanzahl', 'Land',
                                                'Top 10 Länder nach männlicher Bevölkerungszahl im Jahr 2022')
    chart_female = chart_creator.create_bar_chart(countries_female, population_female, 'Bevölkerungsanzahl', 'Land',
                                                  'Top 10 Länder nach weiblicher Bevölkerungszahl im Jahr 2022')

    return render(request, 'geschlechterverhaeltnis.html',
                  {'chart_world_ratio': chart_world_ratio, 'chart_male': chart_male,
                   'chart_female': chart_female,
                   'chart_male_to_female_percentage': chart_male_to_female_percentage,
                   'chart_female_to_male_percentage': chart_female_to_male_percentage})


def home(request):
    """
    Renders the 'home.html' template.
    """
    return render(request, 'home.html')
