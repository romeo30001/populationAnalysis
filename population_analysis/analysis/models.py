from django.db import models


class PopulationData(models.Model):
    country_name = models.CharField(max_length=255)
    country_category = models.CharField(max_length=255)
    country_code = models.CharField(max_length=3)
    indicator_name = models.CharField(max_length=255)
    indicator_code = models.CharField(max_length=50)
    year_1960 = models.BigIntegerField(null=True, blank=True)
    year_1961 = models.BigIntegerField(null=True, blank=True)
    year_1962 = models.BigIntegerField(null=True, blank=True)
    year_1963 = models.BigIntegerField(null=True, blank=True)
    year_1964 = models.BigIntegerField(null=True, blank=True)
    year_1965 = models.BigIntegerField(null=True, blank=True)
    year_1966 = models.BigIntegerField(null=True, blank=True)
    year_1967 = models.BigIntegerField(null=True, blank=True)
    year_1968 = models.BigIntegerField(null=True, blank=True)
    year_1969 = models.BigIntegerField(null=True, blank=True)
    year_1970 = models.BigIntegerField(null=True, blank=True)
    year_1971 = models.BigIntegerField(null=True, blank=True)
    year_1972 = models.BigIntegerField(null=True, blank=True)
    year_1973 = models.BigIntegerField(null=True, blank=True)
    year_1974 = models.BigIntegerField(null=True, blank=True)
    year_1975 = models.BigIntegerField(null=True, blank=True)
    year_1976 = models.BigIntegerField(null=True, blank=True)
    year_1977 = models.BigIntegerField(null=True, blank=True)
    year_1978 = models.BigIntegerField(null=True, blank=True)
    year_1979 = models.BigIntegerField(null=True, blank=True)
    year_1980 = models.BigIntegerField(null=True, blank=True)
    year_1981 = models.BigIntegerField(null=True, blank=True)
    year_1982 = models.BigIntegerField(null=True, blank=True)
    year_1983 = models.BigIntegerField(null=True, blank=True)
    year_1984 = models.BigIntegerField(null=True, blank=True)
    year_1985 = models.BigIntegerField(null=True, blank=True)
    year_1986 = models.BigIntegerField(null=True, blank=True)
    year_1987 = models.BigIntegerField(null=True, blank=True)
    year_1988 = models.BigIntegerField(null=True, blank=True)
    year_1989 = models.BigIntegerField(null=True, blank=True)
    year_1990 = models.BigIntegerField(null=True, blank=True)
    year_1991 = models.BigIntegerField(null=True, blank=True)
    year_1992 = models.BigIntegerField(null=True, blank=True)
    year_1993 = models.BigIntegerField(null=True, blank=True)
    year_1994 = models.BigIntegerField(null=True, blank=True)
    year_1995 = models.BigIntegerField(null=True, blank=True)
    year_1996 = models.BigIntegerField(null=True, blank=True)
    year_1997 = models.BigIntegerField(null=True, blank=True)
    year_1998 = models.BigIntegerField(null=True, blank=True)
    year_1999 = models.BigIntegerField(null=True, blank=True)
    year_2000 = models.BigIntegerField(null=True, blank=True)
    year_2001 = models.BigIntegerField(null=True, blank=True)
    year_2002 = models.BigIntegerField(null=True, blank=True)
    year_2003 = models.BigIntegerField(null=True, blank=True)
    year_2004 = models.BigIntegerField(null=True, blank=True)
    year_2005 = models.BigIntegerField(null=True, blank=True)
    year_2006 = models.BigIntegerField(null=True, blank=True)
    year_2007 = models.BigIntegerField(null=True, blank=True)
    year_2008 = models.BigIntegerField(null=True, blank=True)
    year_2009 = models.BigIntegerField(null=True, blank=True)
    year_2010 = models.BigIntegerField(null=True, blank=True)
    year_2011 = models.BigIntegerField(null=True, blank=True)
    year_2012 = models.BigIntegerField(null=True, blank=True)
    year_2013 = models.BigIntegerField(null=True, blank=True)
    year_2014 = models.BigIntegerField(null=True, blank=True)
    year_2015 = models.BigIntegerField(null=True, blank=True)
    year_2016 = models.BigIntegerField(null=True, blank=True)
    year_2017 = models.BigIntegerField(null=True, blank=True)
    year_2018 = models.BigIntegerField(null=True, blank=True)
    year_2019 = models.BigIntegerField(null=True, blank=True)
    year_2020 = models.BigIntegerField(null=True, blank=True)
    year_2021 = models.BigIntegerField(null=True, blank=True)
    year_2022 = models.BigIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.country_name} - {self.indicator_name}"


class TotalPopulationData(PopulationData):
    class Meta:
        db_table = 'total_population_data'


class FemalePopulationData(PopulationData):
    class Meta:
        db_table = 'female_population_data'


class MalePopulationData(PopulationData):
    class Meta:
        db_table = 'male_population_data'


class OldAgeData(PopulationData):
    class Meta:
        db_table = 'old_age_data'


class MiddleAgeData(PopulationData):
    class Meta:
        db_table = 'middle_age_data'


class YoungAgeData(PopulationData):
    class Meta:
        db_table = 'young_age_data'
