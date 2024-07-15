from django.contrib import admin

from analysis.models import TotalPopulationData, FemalePopulationData, MalePopulationData, OldAgeData, MiddleAgeData, \
    YoungAgeData

# Define a list of models to register with their corresponding Admin classes
models_to_register = [
    (TotalPopulationData, 'Total Population Data'),
    (FemalePopulationData, 'Female Population Data'),
    (MalePopulationData, 'Male Population Data'),
    (OldAgeData, 'Old Age Data'),
    (MiddleAgeData, 'Middle Age Data'),
    (YoungAgeData, 'Young Age Data'),
]


# Custom filter for Country Category
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


# Define a base admin class to reuse settings
class PopulationDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_category', 'year_1960', 'year_2022')
    search_fields = ('country_name', 'country_category', 'year_1960', 'year_2022')
    list_filter = (CountryCategoryFilter,)

    fieldsets = (
        (None, {
            'fields': ('country_name', 'country_code', 'country_category')
        }),
        ('Years', {
            'classes': ('collapse',),
            'fields': tuple(f'year_{year}' for year in range(1960, 2023)),
        }),
    )


# Register models dynamically with their corresponding admin classes
for model, admin_name in models_to_register:
    admin_class = type(f'{model.__name__}Admin', (PopulationDataAdmin,), {})
    admin.site.register(model, admin_class)
