from analysis.models import TotalPopulationData, MalePopulationData, FemalePopulationData, OldAgeData, MiddleAgeData, \
    YoungAgeData
from django.db.models import F, ExpressionWrapper, IntegerField


class PopulationDataFetcher:
    """
    A class to fetch population data from the database.
    """

    @staticmethod
    def get_age_distribution_data():
        old_age_data = OldAgeData.objects.filter(country_name='World').first()
        middle_age_data = MiddleAgeData.objects.filter(country_name='World').first()
        young_age_data = YoungAgeData.objects.filter(country_name='World').first()

        years = list(range(1967, 2023, 5))
        old_population = [getattr(old_age_data, f'year_{year}') for year in years]
        middle_population = [getattr(middle_age_data, f'year_{year}') for year in years]
        young_population = [getattr(young_age_data, f'year_{year}') for year in years]

        return years, old_population, middle_population, young_population

    @staticmethod
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

    @staticmethod
    def get_population_data():
        data = TotalPopulationData.objects.filter(country_category='Country').order_by('-year_2022')[:10]
        countries = [entry.country_name for entry in data]
        population = [entry.year_2022 / 1000000 for entry in data]
        return countries, population

    @staticmethod
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

    @staticmethod
    def get_gender_ratio_data():
        male_data = MalePopulationData.objects.filter(country_name='World').first()
        female_data = FemalePopulationData.objects.filter(country_name='World').first()

        years = list(range(1967, 2023, 5))
        male_population = [getattr(male_data, f'year_{year}') for year in years]
        female_population = [getattr(female_data, f'year_{year}') for year in years]

        return years, male_population, female_population

    @staticmethod
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

    @staticmethod
    def get_top_countries_by_gender_ratio(ratio_type):
        male_data = MalePopulationData.objects.filter(country_category='Country')
        female_data = FemalePopulationData.objects.filter(country_category='Country')

        ratios = []
        if ratio_type == 'male_to_female_percentage':
            for male, female in zip(male_data, female_data):
                total_population = male.year_2022 + female.year_2022
                ratio = (male.year_2022 / total_population) * 100 if total_population != 0 else 0
                ratios.append((male.country_name, ratio))
            ratios = sorted(ratios, key=lambda x: x[1], reverse=True)[:10]
        elif ratio_type == 'female_to_male_percentage':
            for male, female in zip(male_data, female_data):
                total_population = male.year_2022 + female.year_2022
                ratio = (female.year_2022 / total_population) * 100 if total_population != 0 else 0
                ratios.append((female.country_name, ratio))
            ratios = sorted(ratios, key=lambda x: x[1], reverse=True)[:10]

        countries = [x[0] for x in ratios]
        values = [x[1] for x in ratios]
        return countries, values
