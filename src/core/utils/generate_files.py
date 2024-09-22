from src.core.const import CREATE_POSTGRES, CREATE_MySQL

class GenerateFile:
    only_file = None
    data = None

    def __resolve(self, data_export):
        data = [
            {'file_name': 'state', 'data': [], 'fields': ["id", "name", "created_at"]},
            {'file_name': 'cities', 'data': [], 'fields': ["id", "name", "state_id", "created_at"]},
            {'file_name': 'zip_codes', 'data': [], 'fields': ["id", "code", "city_id", "created_at"]}
        ]

        for state in data_export:
            state_id = state['id']
            data[0]['data'].append([state_id, state['state'], "NOW()"])

        for state in data_export:
                for entry in state['cities']:
                    city_id = entry['id']
                    city_name = entry['name']
                    state_id = entry['state_id']
                    data[1]['data'].append([city_id, city_name, state_id, "NOW()"])
        
        for state in data_export:
                for entry in state['cities']:
                    for zipcode in entry['zip_codes']:
                        code= zipcode['code']
                        city_id = zipcode['city_id']
                        data[2]['data'].append([zipcode['id'], code, city_id, "NOW()"])
        self.data = data

    @staticmethod
    def sql(table, fields, values, output, engine):
        syntax = CREATE_POSTGRES if engine == 'postgres' else CREATE_MySQL

        with open(rf"{output}\{table}.sql", 'w', encoding='utf-8') as file:
            for item in values:
                file.write(
                    syntax.format(
                    table,
                    ', '.join(f'"{column}"' for column in fields),
                    ', '.join(f'"{value}"' for value in item)
                    ) + '\n'
                )

    @staticmethod
    def csv(table, fields, values, output):
        with open(rf"{output}\{table}.csv", 'w', encoding='utf-8') as file:
            file.write(','.join(f'{column}' for column in fields) + '\n')
            for item in values:
                file.write(
                    ','.join(f'{value}' for value in item)
                    + '\n'
                )

    def __init__(self, data):
        self.__resolve(data)