from file_util import download_csv, creation_date
import os

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
'Datasheets_stratgems.csv',
'Datasheets_enhancements.csv',
'Datasheets_detachment_abilities.csv',
'Datasheets_leader.csv',
'Stratagems.csv',
'Abilities.csv',
'Enhancements.csv',
'Detachment_abilities.csv',
'Last_update.csv'
]

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_directory)

    for file in wahapedia_files:
        save_path = f'{current_directory}\\csv\\{file}'
        if os.path.isfile(save_path):
            create_date: float = creation_date(save_path)
            print(create_date)
            # TODO redownload files periodically if they are stale
        else:
            download_csv(f'{wahapedia_host}/{wahapedia_system}/{file}', save_path)

if __name__ == "__main__":
    main()