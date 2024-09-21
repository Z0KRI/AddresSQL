import os
import pandas as pd
import uuid
from os.path import isfile, join

class ZipCodes:
    def getFiles(self, path=r'.'):
        states = [
            "AGUASCALIENTES", "BAJA CALIFORNIA", "BAJA CALIFORNIA SUR", "CAMPECHE", "COAHUILA",
            "COLIMA", "CHIAPAS", "CHIHUAHUA", "CIUDAD DE MÉXICO", "DURANGO", "GUANAJUATO",
            "GUERRERO", "HIDALGO", "JALISCO", "MÉXICO", "MICHOACÁN", "MORELOS", "NAYARIT",
            "NUEVO LEÓN", "OAXACA", "PUEBLA", "QUERÉTARO", "QUINTANA ROO", "SAN LUIS POTOSÍ",
            "SINALOA", "SONORA", "TABASCO", "TAMAULIPAS", "TLAXCALA", "VERACRUZ", "YUCATÁN",
            "ZACATECAS"
        ]
        csv_files = [join(path, f"{name.capitalize()}.csv") for name in states if isfile(join(path, f"{name.capitalize()}.csv")) and f"{name.capitalize()}.csv".lower().endswith('.csv')]
        return csv_files
    
    def createSqlDifFiles(self, data):
        states_filename = 'states.sql'
        cities_filename = 'cities.sql'
        zipcodes_filename = 'zipCodes.sql'

        # Escribir inserciones de estados en su archivo correspondiente
        with open(states_filename, 'w', encoding='utf-8') as states_file:
            for state in data:
                state_id = state['id']  # UUID del estado
                state_insert = f"""INSERT INTO "public"."states" ("id", "name", "country_id", "created_at") VALUES ('{state_id}', '{state['state']}', '1', NOW());"""
                states_file.write(state_insert + '\n')

        # Escribir inserciones de ciudades en su archivo correspondiente
        with open(cities_filename, 'w', encoding='utf-8') as cities_file:
            for state in data:
                for entry in state['cities']:
                    city_id = entry['id']  # UUID de la ciudad
                    city_name = entry['City']
                    state_id = entry['stateId']  # UUID del estado asociado

                    city_insert = f"""INSERT INTO "public"."cities" ("id", "name", "state_id", "created_at") VALUES ('{city_id}', '{city_name}', '{state_id}', NOW());"""
                    cities_file.write(city_insert + '\n')

        # Escribir inserciones de códigos postales en su archivo correspondiente
        with open(zipcodes_filename, 'w', encoding='utf-8') as zipcodes_file:
            for state in data:
                for entry in state['cities']:
                    city_id = entry['id']  # UUID de la ciudad
                    for zipcode in entry['zipCodes']:
                        zip_insert = f"""INSERT INTO "public"."zip_codes" ("code", "city_id", "created_at") VALUES ('{zipcode}', '{city_id}', NOW());"""
                        zipcodes_file.write(zip_insert + '\n')
    
    def zipCodes(self, group):
        zip_codes = []
        for _, row in group.iterrows():
            zip_codes.append(row['d_codigo'])
        return zip_codes
    
    def getState(self, item):
        return item.iloc[0]['c_estado']
            
    def groupBy(self, files):
        all_groups = []
        for file in files:
            groups = []
            df = pd.read_csv(file, dtype=str)
            grouped = df.groupby('D_mnpio')
            state_id = str(uuid.uuid4())  # Generar UUID para el estado
            for name, group in grouped:
                city_id = str(uuid.uuid4())  # Generar UUID para la ciudad
                zipCodes = self.zipCodes(group)
                groups.append({'id': city_id, 'City': name, 'zipCodes': zipCodes, 'stateId': state_id})
            all_groups.append({'id': state_id, 'state': os.path.splitext(os.path.basename(file))[0], "cities": groups})
        return all_groups
    
    def __init__(self):
        files = self.getFiles()
        cities = self.groupBy(files)
        self.createSqlDifFiles(cities)

ZipCodes()
