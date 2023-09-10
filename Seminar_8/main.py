from File_manager.create_file_txt import create_file_txt
from File_manager.txt_to_json import txt_to_json
from File_manager.create_file_json import  func
from File_manager.json_to_csv import json_to_csv
from File_manager.csv_to_json import csv_to_json
from File_manager.directory_reference import directory_reference

from pathlib import Path

if __name__ == '__main__':

    create_file_txt('data.txt', 'w')
    for _ in range(10):
        create_file_txt('data.txt', 'a')

    txt_to_json('data.txt', 'data.json')
    func('data1.json')
    json_to_csv('data1.json', 'data.csv')
    csv_to_json('data.csv', 'data2.json')
    directory_reference(Path(Path.cwd()))