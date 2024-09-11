import os
import time

from file_util import download_csv, creation_date

wahapedia_host = 'http://wahapedia.ru/'
wahapedia_system = 'wh40k10ed'
wahapedia_files = [
    'Factions.csv',
    'Source.csv',
    'Datasheets.csv',
    'Datasheets_abilities.csv',
    'Datasheets_keywords.csv',
    'Datasheets_models.csv',
    'Datasheets_options.csv',
    'Datasheets_wargear.csv',
    'Datasheets_unit_composition.csv',
    'Datasheets_models_cost.csv',
    'Datasheets_stratagems.csv',
    'Datasheets_enhancements.csv',
    'Datasheets_detachment_abilities.csv',
    'Datasheets_leader.csv',
    'Stratagems.csv',
    'Abilities.csv',
    'Enhancements.csv',
    'Detachment_abilities.csv',
    'Last_update.csv'
]

# Re-download csv files every X seconds
refresh_rate_in_seconds = 7 * 24 * 60 * 60  # 7 days * 24 hours * 60 minutes * 60 seconds
working_directory = os.path.dirname(os.path.abspath(__file__))

def init_csv_files():
    now = int(time.time())

    for file in wahapedia_files:
        local_path = f'{working_directory}\\csv\\{file}'
        remote_path = f'{wahapedia_host}/{wahapedia_system}/{file}'

        # If file doesn't exist, download it
        if not os.path.isfile(local_path):
            download_csv(remote_path, local_path)
            continue

        # If file is expired, re-download it
        create_date: int = creation_date(local_path)
        elapsed_seconds = now - create_date
        if elapsed_seconds > refresh_rate_in_seconds:
            print(f'{local_path} is {elapsed_seconds} seconds past the max expiration time of {refresh_rate_in_seconds} seconds')
            download_csv(remote_path, local_path)

if __name__ == "__main__":
    init_csv_files()
