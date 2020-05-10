
from helpers.args import COL_SIZE


def run(raw_data: dict, src_file: str, max_date: str) -> dict:
    if raw_data and len(raw_data) and len(raw_data[0]) == COL_SIZE:
        return raw_data
    else:
        raise FileNotFoundError(
            'Invalid file contents {0} check csv format: (INVESTMENT DATE, SHARES PURCHASED, CASH PAID, INVESTOR NAME)'.format(src_file))
