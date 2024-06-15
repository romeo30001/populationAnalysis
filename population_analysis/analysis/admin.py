from django.contrib import admin

from analysis.models import TotalPopulationData, FemalePopulationData, MalePopulationData, OldAgeData, MiddleAgeData, \
    YoungAgeData


class CountryCategoryFilter(admin.SimpleListFilter):
    title = 'Country Category'
    parameter_name = 'country_category'

    def lookups(self, request, model_admin):
        return (
            ('Country', 'Country'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Country':
            return queryset.filter(country_category='Country')


# Register your models here.
@admin.register(TotalPopulationData)
class TotalPopulationDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': (
                'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
                'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969',
                'year_1970', 'year_1971', 'year_1972', 'year_1973', 'year_1974',
                'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979',
                'year_1980', 'year_1981', 'year_1982', 'year_1983', 'year_1984',
                'year_1985', 'year_1986', 'year_1987', 'year_1988', 'year_1989',
                'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994',
                'year_1995', 'year_1996', 'year_1997', 'year_1998', 'year_1999',
                'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019',
                'year_2020', 'year_2021', 'year_2022'
            ),
        }),
    )


@admin.register(FemalePopulationData)
class FemalePopulationDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': (
                'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
                'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969',
                'year_1970', 'year_1971', 'year_1972', 'year_1973', 'year_1974',
                'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979',
                'year_1980', 'year_1981', 'year_1982', 'year_1983', 'year_1984',
                'year_1985', 'year_1986', 'year_1987', 'year_1988', 'year_1989',
                'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994',
                'year_1995', 'year_1996', 'year_1997', 'year_1998', 'year_1999',
                'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019',
                'year_2020', 'year_2021', 'year_2022'
            ),
        }),
    )


@admin.register(MalePopulationData)
class MalePopulationDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': (
                'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
                'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969',
                'year_1970', 'year_1971', 'year_1972', 'year_1973', 'year_1974',
                'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979',
                'year_1980', 'year_1981', 'year_1982', 'year_1983', 'year_1984',
                'year_1985', 'year_1986', 'year_1987', 'year_1988', 'year_1989',
                'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994',
                'year_1995', 'year_1996', 'year_1997', 'year_1998', 'year_1999',
                'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019',
                'year_2020', 'year_2021', 'year_2022'
            ),
        }),
    )


@admin.register(OldAgeData)
class OldAgeDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': (
                'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
                'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969',
                'year_1970', 'year_1971', 'year_1972', 'year_1973', 'year_1974',
                'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979',
                'year_1980', 'year_1981', 'year_1982', 'year_1983', 'year_1984',
                'year_1985', 'year_1986', 'year_1987', 'year_1988', 'year_1989',
                'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994',
                'year_1995', 'year_1996', 'year_1997', 'year_1998', 'year_1999',
                'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019',
                'year_2020', 'year_2021', 'year_2022'
            ),
        }),
    )


@admin.register(MiddleAgeData)
class MiddleAgeDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': (
                'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
                'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969',
                'year_1970', 'year_1971', 'year_1972', 'year_1973', 'year_1974',
                'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979',
                'year_1980', 'year_1981', 'year_1982', 'year_1983', 'year_1984',
                'year_1985', 'year_1986', 'year_1987', 'year_1988', 'year_1989',
                'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994',
                'year_1995', 'year_1996', 'year_1997', 'year_1998', 'year_1999',
                'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019',
                'year_2020', 'year_2021', 'year_2022'
            ),
        }),
    )


@admin.register(YoungAgeData)
class YoungAgeDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': (
                'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
                'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969',
                'year_1970', 'year_1971', 'year_1972', 'year_1973', 'year_1974',
                'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979',
                'year_1980', 'year_1981', 'year_1982', 'year_1983', 'year_1984',
                'year_1985', 'year_1986', 'year_1987', 'year_1988', 'year_1989',
                'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994',
                'year_1995', 'year_1996', 'year_1997', 'year_1998', 'year_1999',
                'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019',
                'year_2020', 'year_2021', 'year_2022'
            ),
        }),
    )
