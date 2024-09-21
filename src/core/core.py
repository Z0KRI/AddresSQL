from .const import STATES

from src.core.utils.generate_files import GenerateFile

from os.path import isfile, join
import pandas as pd
import uuid
import os

class Core:
    def __getFiles(self, path):
        csv_files = [join(path, f"{name.capitalize()}.csv") for name in STATES if isfile(join(path, f"{name.capitalize()}.csv")) and f"{name.capitalize()}.csv".lower().endswith('.csv')]
        return csv_files
    
    def __get_data(self, files):
        #? Se encarga de iterar los archivos para obtener la data
        data = [self.__process_file(file) for file in files]
        return data

    def __process_file(self, file):
        df = pd.read_csv(file, dtype=str)
        grouped = df.groupby('D_mnpio')
        state_id = str(uuid.uuid4())

        cities = [self.__process_city(name, group, state_id) for name, group in grouped]

        return {
            'id': state_id,
            'state': os.path.splitext(os.path.basename(file))[0],
            'cities': cities
        }
    
    def __process_city(self, city_name, group, state_id):
        city_id = str(uuid.uuid4())

        zip_codes = [
            {'id': str(uuid.uuid4()), 
            'code': row['d_codigo'],
            'city_id': city_id} for _, row in group.iterrows()]
        return {
            'id': city_id,
            'name': city_name,
            'state_id': state_id,
            'zip_codes': zip_codes
        }

    def export_data(self, data, args):
        genFile = GenerateFile(data)

        for item in genFile.data:
            if args.type == 'sql':
                if args.engine == 'postgres':
                    genFile.sql(table=item['file_name'], fields=item['fields'], values=item['data'], output=args.output, engine=args.engine)
                elif args.engine == 'mysql':
                    print(item['file_name'])
            else:
                genFile.csv(table=item['file_name'], fields=item['fields'], values=item['data'], output=args.output)

    
    def __init__(self, args):
        print(args)
        files = self.__getFiles(args.path)
        data = self.__get_data(files)
        self.export_data(data, args)
