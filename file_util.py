import requests
import os
import platform
import csv

def download_csv(url, save_path):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Write the content to a file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded and saved to {save_path}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

def csv_to_dict(file_path):
    result = {}
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            first_column_value = next(iter(row.values()))
            result[first_column_value] = row
    return result

def creation_date(path_to_file) -> int:
    if platform.system() == 'Windows':
        return int(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            return int(stat.st_birthtime)
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return int(stat.st_mtime)