import argparse
import os.path

from datetime import datetime

COL_SIZE = 4


def setup_argparser() -> argparse.ArgumentParser:
    '''
    Parse args and return variables containing values, for testing purposes.
    '''

    parser = argparse.ArgumentParser(
        description='Compute and print out a captable summary from a csv file')

    parser.add_argument('--src-file', dest='src_file', action='store', required=True,
                        help='Path of CSV file containing captable entries (REQUIRED)')

    parser.add_argument('--max-date', dest='max_date', action='store', required=False,
                        default=datetime.now().strftime("%Y-%m-%d"),
                        help='Max date of captable summary (YYYY-MM-DD). Default Today (OPTIONAL)')

    return parser


def validate_date(date: str) -> str:
    '''
        Validate date value and check if is not in the future
    '''

    try:
        date = datetime.strptime(date, "%Y-%m-%d")

        if date > datetime.now():
            raise argparse.ArgumentTypeError(
                'Max date arg can´t be in the future')
        else:
            return date
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Not a valid date: '{0}'.".format(date))


def validate_file(path_: str) -> bool:
    '''
        check if a file exists
    '''

    if path_ and os.path.isfile(path_):
        return True
    else:
        raise argparse.ArgumentTypeError(
            'File does not exist {0}'.format(path_))
