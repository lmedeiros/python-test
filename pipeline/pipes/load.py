import csv


def run(raw_data: dict, src_file: str, max_date: str) -> dict:
    '''
    Load csv file into dict, and remove header (1st line)
    '''
    with open(src_file) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        return [row for row in csv_reader][1:]
