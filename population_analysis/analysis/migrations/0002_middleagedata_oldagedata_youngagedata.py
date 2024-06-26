# Generated by Django 5.0.6 on 2024-06-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiddleAgeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_category', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=3)),
                ('indicator_name', models.CharField(max_length=255)),
                ('indicator_code', models.CharField(max_length=50)),
                ('year_1960', models.BigIntegerField(blank=True, null=True)),
                ('year_1961', models.BigIntegerField(blank=True, null=True)),
                ('year_1962', models.BigIntegerField(blank=True, null=True)),
                ('year_1963', models.BigIntegerField(blank=True, null=True)),
                ('year_1964', models.BigIntegerField(blank=True, null=True)),
                ('year_1965', models.BigIntegerField(blank=True, null=True)),
                ('year_1966', models.BigIntegerField(blank=True, null=True)),
                ('year_1967', models.BigIntegerField(blank=True, null=True)),
                ('year_1968', models.BigIntegerField(blank=True, null=True)),
                ('year_1969', models.BigIntegerField(blank=True, null=True)),
                ('year_1970', models.BigIntegerField(blank=True, null=True)),
                ('year_1971', models.BigIntegerField(blank=True, null=True)),
                ('year_1972', models.BigIntegerField(blank=True, null=True)),
                ('year_1973', models.BigIntegerField(blank=True, null=True)),
                ('year_1974', models.BigIntegerField(blank=True, null=True)),
                ('year_1975', models.BigIntegerField(blank=True, null=True)),
                ('year_1976', models.BigIntegerField(blank=True, null=True)),
                ('year_1977', models.BigIntegerField(blank=True, null=True)),
                ('year_1978', models.BigIntegerField(blank=True, null=True)),
                ('year_1979', models.BigIntegerField(blank=True, null=True)),
                ('year_1980', models.BigIntegerField(blank=True, null=True)),
                ('year_1981', models.BigIntegerField(blank=True, null=True)),
                ('year_1982', models.BigIntegerField(blank=True, null=True)),
                ('year_1983', models.BigIntegerField(blank=True, null=True)),
                ('year_1984', models.BigIntegerField(blank=True, null=True)),
                ('year_1985', models.BigIntegerField(blank=True, null=True)),
                ('year_1986', models.BigIntegerField(blank=True, null=True)),
                ('year_1987', models.BigIntegerField(blank=True, null=True)),
                ('year_1988', models.BigIntegerField(blank=True, null=True)),
                ('year_1989', models.BigIntegerField(blank=True, null=True)),
                ('year_1990', models.BigIntegerField(blank=True, null=True)),
                ('year_1991', models.BigIntegerField(blank=True, null=True)),
                ('year_1992', models.BigIntegerField(blank=True, null=True)),
                ('year_1993', models.BigIntegerField(blank=True, null=True)),
                ('year_1994', models.BigIntegerField(blank=True, null=True)),
                ('year_1995', models.BigIntegerField(blank=True, null=True)),
                ('year_1996', models.BigIntegerField(blank=True, null=True)),
                ('year_1997', models.BigIntegerField(blank=True, null=True)),
                ('year_1998', models.BigIntegerField(blank=True, null=True)),
                ('year_1999', models.BigIntegerField(blank=True, null=True)),
                ('year_2000', models.BigIntegerField(blank=True, null=True)),
                ('year_2001', models.BigIntegerField(blank=True, null=True)),
                ('year_2002', models.BigIntegerField(blank=True, null=True)),
                ('year_2003', models.BigIntegerField(blank=True, null=True)),
                ('year_2004', models.BigIntegerField(blank=True, null=True)),
                ('year_2005', models.BigIntegerField(blank=True, null=True)),
                ('year_2006', models.BigIntegerField(blank=True, null=True)),
                ('year_2007', models.BigIntegerField(blank=True, null=True)),
                ('year_2008', models.BigIntegerField(blank=True, null=True)),
                ('year_2009', models.BigIntegerField(blank=True, null=True)),
                ('year_2010', models.BigIntegerField(blank=True, null=True)),
                ('year_2011', models.BigIntegerField(blank=True, null=True)),
                ('year_2012', models.BigIntegerField(blank=True, null=True)),
                ('year_2013', models.BigIntegerField(blank=True, null=True)),
                ('year_2014', models.BigIntegerField(blank=True, null=True)),
                ('year_2015', models.BigIntegerField(blank=True, null=True)),
                ('year_2016', models.BigIntegerField(blank=True, null=True)),
                ('year_2017', models.BigIntegerField(blank=True, null=True)),
                ('year_2018', models.BigIntegerField(blank=True, null=True)),
                ('year_2019', models.BigIntegerField(blank=True, null=True)),
                ('year_2020', models.BigIntegerField(blank=True, null=True)),
                ('year_2021', models.BigIntegerField(blank=True, null=True)),
                ('year_2022', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OldAgeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_category', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=3)),
                ('indicator_name', models.CharField(max_length=255)),
                ('indicator_code', models.CharField(max_length=50)),
                ('year_1960', models.BigIntegerField(blank=True, null=True)),
                ('year_1961', models.BigIntegerField(blank=True, null=True)),
                ('year_1962', models.BigIntegerField(blank=True, null=True)),
                ('year_1963', models.BigIntegerField(blank=True, null=True)),
                ('year_1964', models.BigIntegerField(blank=True, null=True)),
                ('year_1965', models.BigIntegerField(blank=True, null=True)),
                ('year_1966', models.BigIntegerField(blank=True, null=True)),
                ('year_1967', models.BigIntegerField(blank=True, null=True)),
                ('year_1968', models.BigIntegerField(blank=True, null=True)),
                ('year_1969', models.BigIntegerField(blank=True, null=True)),
                ('year_1970', models.BigIntegerField(blank=True, null=True)),
                ('year_1971', models.BigIntegerField(blank=True, null=True)),
                ('year_1972', models.BigIntegerField(blank=True, null=True)),
                ('year_1973', models.BigIntegerField(blank=True, null=True)),
                ('year_1974', models.BigIntegerField(blank=True, null=True)),
                ('year_1975', models.BigIntegerField(blank=True, null=True)),
                ('year_1976', models.BigIntegerField(blank=True, null=True)),
                ('year_1977', models.BigIntegerField(blank=True, null=True)),
                ('year_1978', models.BigIntegerField(blank=True, null=True)),
                ('year_1979', models.BigIntegerField(blank=True, null=True)),
                ('year_1980', models.BigIntegerField(blank=True, null=True)),
                ('year_1981', models.BigIntegerField(blank=True, null=True)),
                ('year_1982', models.BigIntegerField(blank=True, null=True)),
                ('year_1983', models.BigIntegerField(blank=True, null=True)),
                ('year_1984', models.BigIntegerField(blank=True, null=True)),
                ('year_1985', models.BigIntegerField(blank=True, null=True)),
                ('year_1986', models.BigIntegerField(blank=True, null=True)),
                ('year_1987', models.BigIntegerField(blank=True, null=True)),
                ('year_1988', models.BigIntegerField(blank=True, null=True)),
                ('year_1989', models.BigIntegerField(blank=True, null=True)),
                ('year_1990', models.BigIntegerField(blank=True, null=True)),
                ('year_1991', models.BigIntegerField(blank=True, null=True)),
                ('year_1992', models.BigIntegerField(blank=True, null=True)),
                ('year_1993', models.BigIntegerField(blank=True, null=True)),
                ('year_1994', models.BigIntegerField(blank=True, null=True)),
                ('year_1995', models.BigIntegerField(blank=True, null=True)),
                ('year_1996', models.BigIntegerField(blank=True, null=True)),
                ('year_1997', models.BigIntegerField(blank=True, null=True)),
                ('year_1998', models.BigIntegerField(blank=True, null=True)),
                ('year_1999', models.BigIntegerField(blank=True, null=True)),
                ('year_2000', models.BigIntegerField(blank=True, null=True)),
                ('year_2001', models.BigIntegerField(blank=True, null=True)),
                ('year_2002', models.BigIntegerField(blank=True, null=True)),
                ('year_2003', models.BigIntegerField(blank=True, null=True)),
                ('year_2004', models.BigIntegerField(blank=True, null=True)),
                ('year_2005', models.BigIntegerField(blank=True, null=True)),
                ('year_2006', models.BigIntegerField(blank=True, null=True)),
                ('year_2007', models.BigIntegerField(blank=True, null=True)),
                ('year_2008', models.BigIntegerField(blank=True, null=True)),
                ('year_2009', models.BigIntegerField(blank=True, null=True)),
                ('year_2010', models.BigIntegerField(blank=True, null=True)),
                ('year_2011', models.BigIntegerField(blank=True, null=True)),
                ('year_2012', models.BigIntegerField(blank=True, null=True)),
                ('year_2013', models.BigIntegerField(blank=True, null=True)),
                ('year_2014', models.BigIntegerField(blank=True, null=True)),
                ('year_2015', models.BigIntegerField(blank=True, null=True)),
                ('year_2016', models.BigIntegerField(blank=True, null=True)),
                ('year_2017', models.BigIntegerField(blank=True, null=True)),
                ('year_2018', models.BigIntegerField(blank=True, null=True)),
                ('year_2019', models.BigIntegerField(blank=True, null=True)),
                ('year_2020', models.BigIntegerField(blank=True, null=True)),
                ('year_2021', models.BigIntegerField(blank=True, null=True)),
                ('year_2022', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoungAgeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_category', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=3)),
                ('indicator_name', models.CharField(max_length=255)),
                ('indicator_code', models.CharField(max_length=50)),
                ('year_1960', models.BigIntegerField(blank=True, null=True)),
                ('year_1961', models.BigIntegerField(blank=True, null=True)),
                ('year_1962', models.BigIntegerField(blank=True, null=True)),
                ('year_1963', models.BigIntegerField(blank=True, null=True)),
                ('year_1964', models.BigIntegerField(blank=True, null=True)),
                ('year_1965', models.BigIntegerField(blank=True, null=True)),
                ('year_1966', models.BigIntegerField(blank=True, null=True)),
                ('year_1967', models.BigIntegerField(blank=True, null=True)),
                ('year_1968', models.BigIntegerField(blank=True, null=True)),
                ('year_1969', models.BigIntegerField(blank=True, null=True)),
                ('year_1970', models.BigIntegerField(blank=True, null=True)),
                ('year_1971', models.BigIntegerField(blank=True, null=True)),
                ('year_1972', models.BigIntegerField(blank=True, null=True)),
                ('year_1973', models.BigIntegerField(blank=True, null=True)),
                ('year_1974', models.BigIntegerField(blank=True, null=True)),
                ('year_1975', models.BigIntegerField(blank=True, null=True)),
                ('year_1976', models.BigIntegerField(blank=True, null=True)),
                ('year_1977', models.BigIntegerField(blank=True, null=True)),
                ('year_1978', models.BigIntegerField(blank=True, null=True)),
                ('year_1979', models.BigIntegerField(blank=True, null=True)),
                ('year_1980', models.BigIntegerField(blank=True, null=True)),
                ('year_1981', models.BigIntegerField(blank=True, null=True)),
                ('year_1982', models.BigIntegerField(blank=True, null=True)),
                ('year_1983', models.BigIntegerField(blank=True, null=True)),
                ('year_1984', models.BigIntegerField(blank=True, null=True)),
                ('year_1985', models.BigIntegerField(blank=True, null=True)),
                ('year_1986', models.BigIntegerField(blank=True, null=True)),
                ('year_1987', models.BigIntegerField(blank=True, null=True)),
                ('year_1988', models.BigIntegerField(blank=True, null=True)),
                ('year_1989', models.BigIntegerField(blank=True, null=True)),
                ('year_1990', models.BigIntegerField(blank=True, null=True)),
                ('year_1991', models.BigIntegerField(blank=True, null=True)),
                ('year_1992', models.BigIntegerField(blank=True, null=True)),
                ('year_1993', models.BigIntegerField(blank=True, null=True)),
                ('year_1994', models.BigIntegerField(blank=True, null=True)),
                ('year_1995', models.BigIntegerField(blank=True, null=True)),
                ('year_1996', models.BigIntegerField(blank=True, null=True)),
                ('year_1997', models.BigIntegerField(blank=True, null=True)),
                ('year_1998', models.BigIntegerField(blank=True, null=True)),
                ('year_1999', models.BigIntegerField(blank=True, null=True)),
                ('year_2000', models.BigIntegerField(blank=True, null=True)),
                ('year_2001', models.BigIntegerField(blank=True, null=True)),
                ('year_2002', models.BigIntegerField(blank=True, null=True)),
                ('year_2003', models.BigIntegerField(blank=True, null=True)),
                ('year_2004', models.BigIntegerField(blank=True, null=True)),
                ('year_2005', models.BigIntegerField(blank=True, null=True)),
                ('year_2006', models.BigIntegerField(blank=True, null=True)),
                ('year_2007', models.BigIntegerField(blank=True, null=True)),
                ('year_2008', models.BigIntegerField(blank=True, null=True)),
                ('year_2009', models.BigIntegerField(blank=True, null=True)),
                ('year_2010', models.BigIntegerField(blank=True, null=True)),
                ('year_2011', models.BigIntegerField(blank=True, null=True)),
                ('year_2012', models.BigIntegerField(blank=True, null=True)),
                ('year_2013', models.BigIntegerField(blank=True, null=True)),
                ('year_2014', models.BigIntegerField(blank=True, null=True)),
                ('year_2015', models.BigIntegerField(blank=True, null=True)),
                ('year_2016', models.BigIntegerField(blank=True, null=True)),
                ('year_2017', models.BigIntegerField(blank=True, null=True)),
                ('year_2018', models.BigIntegerField(blank=True, null=True)),
                ('year_2019', models.BigIntegerField(blank=True, null=True)),
                ('year_2020', models.BigIntegerField(blank=True, null=True)),
                ('year_2021', models.BigIntegerField(blank=True, null=True)),
                ('year_2022', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
