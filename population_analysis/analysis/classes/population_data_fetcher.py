from analysis.models import TotalPopulationData, MalePopulationData, FemalePopulationData, OldAgeData, MiddleAgeData, \
    YoungAgeData
from django.db.models import F, ExpressionWrapper, IntegerField


class PopulationDataFetcher:
    """
    A class to fetch population data from the database.
    """

    def __init__(self, country='World', year=2022):
        """
        :param country: The name of the country. Defaults to 'World'.
        :param year: The year for which data is fetched. Defaults to 2022.
        """
        self.country = country
        self.year = year

    def get_age_distribution_data(self):
        """
        Retrieves age distribution data for the world population across years.

        :return: Tuple of lists (years, old_population, middle_population, young_population).
                 - years: List of years from 1967 to 2022 (every 5 years).
                 - old_population: List of population data for old age category across the years.
                 - middle_population: List of population data for middle age category across the years.
                 - young_population: List of population data for young age category across the years.
        """
        old_age_data = OldAgeData.objects.filter(country_name=self.country).first()
        middle_age_data = MiddleAgeData.objects.filter(country_name=self.country).first()
        young_age_data = YoungAgeData.objects.filter(country_name=self.country).first()

        years = list(range(1967, 2023, 5))
        old_population = [getattr(old_age_data, f'year_{year}') for year in years]
        middle_population = [getattr(middle_age_data, f'year_{year}') for year in years]
        young_population = [getattr(young_age_data, f'year_{year}') for year in years]

        return years, old_population, middle_population, young_population

    def get_top_ten_countries_data(self, category):
        """
        Retrieves population data for the top 10 most populated countries.

        :return: Tuple of lists (countries, population).
                 - countries: List of country names.
                 - population: List of population data (in millions) for the top 10 countries and the specified year.
        """
        if category == "old":
            data = OldAgeData.objects.filter(country_category='Country').order_by(f'-year_{self.year}')[:10]
        elif category == "middle":
            data = MiddleAgeData.objects.filter(country_category='Country').order_by(f'-year_{self.year}')[:10]
        else:
            data = YoungAgeData.objects.filter(country_category='Country').order_by(f'-year_{self.year}')[:10]

        countries = [entry.country_name for entry in data]
        population = [getattr(entry, f'year_{self.year}') / 1000000 for entry in data]
        return countries, population

    def get_population_data(self):
        """
        Retrieves population data for the top 10 most populated countries.

        :return: Tuple of lists (countries, population).
                 - countries: List of country names.
                 - population: List of population data (in millions) for the top 10 countries and the specified year.
        """
        data = TotalPopulationData.objects.filter(country_category='Country').order_by(f'-year_{self.year}')[:10]
        countries = [entry.country_name for entry in data]
        population = [getattr(entry, f'year_{self.year}') / 1000000 for entry in data]
        return countries, population

    def get_population_growth_data(self, years):
        """
        Retrieves population growth data for the top 10 countries over a specified period (10 or 60 years).

        :param years: The period of years for which population growth is calculated (10 or 60).
        :return: Tuple of lists (countries, population).
                 - countries: List of country names.
                 - population: List of population growth data (in millions) for the top 10 countries over the specified period.
        """
        data = TotalPopulationData.objects.filter(country_category='Country')

        if years == 10:
            data = data.annotate(
                population_difference=ExpressionWrapper(
                    (F(f'year_{self.year}') - F(f'year_{self.year - 9}')) / 1000000,
                    output_field=IntegerField()
                )
            ).order_by('-population_difference')[:10]
        else:
            data = data.annotate(
                population_difference=ExpressionWrapper(
                    (F(f'year_{self.year}') - F(f'year_{self.year - 59}')) / 1000000,
                    output_field=IntegerField()
                )
            ).order_by('-population_difference')[:10]

        countries = [entry.country_name for entry in data]
        population = [entry.population_difference for entry in data]
        return countries, population

    def get_gender_ratio_data(self):
        """
        Retrieves gender ratio data for the world population across years.

        :return: Tuple of lists (years, male_population, female_population).
                 - years: List of years from 1967 to 2022 (every 5 years).
                 - male_population: List of male population data across the years.
                 - female_population: List of female population data across the years.
        """
        male_data = MalePopulationData.objects.filter(country_name=self.country).first()
        female_data = FemalePopulationData.objects.filter(country_name=self.country).first()

        years = list(range(1967, 2023, 5))
        male_population = [getattr(male_data, f'year_{year}') for year in years]
        female_population = [getattr(female_data, f'year_{year}') for year in years]

        return years, male_population, female_population

    def get_top_ten_countries_gender(self, category):
        """
        Retrieves population data for the top 10 countries based on a specified gender (male or female).

        :param category: The gender category ('male' or 'female').
        :return: Tuple of lists (countries, population).
                 - countries: List of country names.
                 - population: List of population data (in millions) for the top 10 countries and the specified gender.
        """
        if category == "male":
            data = MalePopulationData.objects.filter(country_category='Country').order_by(f'-year_{self.year}')[:10]
        else:
            data = FemalePopulationData.objects.filter(country_category='Country').order_by(f'-year_{self.year}')[:10]

        countries = [entry.country_name for entry in data]
        population = [getattr(entry, f'year_{self.year}') / 1000000 for entry in data]
        return countries, population

    def get_top_countries_by_gender_ratio(self, ratio_type):
        """
        Calculates and retrieves data for the top 10 countries with the highest gender ratio (male-to-female or female-to-male).

        :param ratio_type: The type of gender ratio to calculate ('male_to_female_percentage' or 'female_to_male_percentage').
        :return: Tuple of lists (countries, values).
                 - countries: List of country names.
                 - values: List of gender ratio values for the top 10 countries.
        """
        male_data = MalePopulationData.objects.filter(country_category='Country')
        female_data = FemalePopulationData.objects.filter(country_category='Country')

        ratios = []
        if ratio_type == 'male_to_female_percentage':
            for male, female in zip(male_data, female_data):
                total_population = getattr(male, f'year_{self.year}') + getattr(female, f'year_{self.year}')
                ratio = (getattr(male, f'year_{self.year}') / total_population) * 100 if total_population != 0 else 0
                ratios.append((male.country_name, ratio))
            ratios = sorted(ratios, key=lambda x: x[1], reverse=True)[:10]
        elif ratio_type == 'female_to_male_percentage':
            for male, female in zip(male_data, female_data):
                total_population = getattr(male, f'year_{self.year}') + getattr(female, f'year_{self.year}')
                ratio = (getattr(female, f'year_{self.year}') / total_population) * 100 if total_population != 0 else 0
                ratios.append((female.country_name, ratio))
            ratios = sorted(ratios, key=lambda x: x[1], reverse=True)[:10]

        countries = [x[0] for x in ratios]
        values = [x[1] for x in ratios]
        return countries, values
