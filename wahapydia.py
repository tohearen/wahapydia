import os
import time

from file_util import download_csv, creation_date, csv_to_dict

wahapedia_host = 'http://wahapedia.ru/'
wahapedia_system = 'wh40k10ed'
wahapedia_files = [
    'Factions',
    'Source',
    'Datasheets',
    'Datasheets_abilities',
    'Datasheets_keywords',
    'Datasheets_models',
    'Datasheets_options',
    'Datasheets_wargear',
    'Datasheets_unit_composition',
    'Datasheets_models_cost',
    'Datasheets_stratagems',
    'Datasheets_enhancements',
    'Datasheets_detachment_abilities',
    'Datasheets_leader',
    'Stratagems',
    'Abilities',
    'Enhancements',
    'Detachment_abilities',
    'Last_update'
]

# Re-download csv files every X seconds
refresh_rate_in_seconds = 7 * 24 * 60 * 60  # 7 days * 24 hours * 60 minutes * 60 seconds

# Key: local path, Value: remote path
def get_csv_paths() -> {str, str}:
    all_paths = {}
    working_directory = os.path.dirname(os.path.abspath(__file__))
    for file in wahapedia_files:
        all_paths[file] = {
            'remote' : f'{wahapedia_host}/{wahapedia_system}/{file}.csv',
            'local' : f'{working_directory}\\csv\\{file}.csv'
        }
    return all_paths


csv_paths = get_csv_paths()


def download_csv_files():
    now = int(time.time())

    for key in csv_paths:
        remote_path = csv_paths[key]['remote']
        local_path = csv_paths[key]['local']


        # If file doesn't exist, download it
        if not os.path.isfile(local_path):
            download_csv(remote_path, local_path)
            continue

        # If file is expired, re-download it
        create_date: int = creation_date(local_path)
        elapsed_seconds = now - create_date
        if elapsed_seconds > refresh_rate_in_seconds:
            print(
                f'{local_path} is {elapsed_seconds} seconds past the max expiration time of {refresh_rate_in_seconds} seconds')
            download_csv(remote_path, local_path)

def read_csv_files():
    files = {}
    for key in csv_paths:
        result = csv_to_dict(csv_paths[key]['local'])
        files[key] = result
    return files

if __name__ == "__main__":
    result = read_csv_files()
    print(result)
    print('')
