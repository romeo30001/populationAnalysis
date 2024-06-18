# Analysis and Visualization of World Population Development with Django

## Author information
Author: Roman Fen
Class: FI-C26

## Project Goal
The goal of this project is to develop a web application that collects, processes, and visualizes historical and current population data of various countries and regions. The application aims to enable users to analyze population growth, trends, and to make forecasts.

## Project Description
### 1. Data Source and Collection
- Collect population data from the World Bank.
- Store the data in a local database.

### 2. Data Processing
- Clean and normalize the collected data.
- Calculate metrics such as growth rates, age distribution, and gender ratio.

### 3. Data Visualization
- Develop a web application to display population data.
- Integrate charts to visualize the data.

## Table of Contents
- [Author information](#author-information)
- [Project Goal](#project-goal)
- [Project Description](#project-description)
- [Requirements](#requirements)
- [Importing the Database](#importing-the-database)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [References](#references)


## Requirements
- Python 3.10+
- Django 5.0+
- PostgreSQL 14.12+

## Importing the Database
1. Ensure PostgreSQL is installed and running on your system.

2. Create the database if it does not exist:
    ```sh
    createdb -h localhost -U your_db_user your_db_name
    ```

3. Import the `database.sql` file into your PostgreSQL database:
    ```sh
    psql -h localhost -U your_db_user -d your_db_name -f path/to/database.sql
    ```
    Replace `your_db_user`, `your_db_name`, and `path/to/database.sql` with your PostgreSQL username, database name, and the path to your `database.sql` file, respectively. You will be prompted to enter your database password.

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:romeo30001/populationAnalysis.git 
    cd populationAnalysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```


## Configuration
1. Copy the `.env.example` file to `.env` and configure the environment variables:
    ```sh
    cp .env.example .env
    ```

2. Fill in the `.env` file with the necessary values:
    ```ini
    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=django_allowed_hosts

    # Database settings
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    ```

## Running the Project
1. Start the development server:
    ```sh
    python manage.py runserver
    ```

2. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


Once the server is running, you can use the application to:
- Analyze population growth, trends, and forecasts through various charts.

## References
1. Django documentation: https://docs.djangoproject.com/en/5.0/
2. Matplotlib documentation: https://matplotlib.org/stable/index.html
3. Postgresql documentation: https://www.postgresql.org/files/documentation/pdf/14/postgresql-14-A4.pdf
4. Venv documentation: https://docs.python.org/3/library/venv.html
5. Python documentation: https://docs.python.org/3/
6. World Bank Population Data: https://data.worldbank.org/indicator/SP.POP.TOTL