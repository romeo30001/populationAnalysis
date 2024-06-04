import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


# Verbindung zur PostgreSQL-Datenbank
engine = create_engine('postgresql://roman:@localhost:5432/population_analysis')

# Pfad zur hochgeladenen Datei
file_path = 'analysis/data/population_total.csv'

# Lesen der CSV-Datei
data = pd.read_csv(file_path)

try:
    # Speichern der Daten in der PostgreSQL-Datenbank
    data.to_sql('analysis_populationdata', engine, if_exists='replace', index=False)
    print("Daten erfolgreich in die Datenbank gespeichert.")
except SQLAlchemyError as e:
    print("Fehler beim Speichern der Daten in die Datenbank:", e)
