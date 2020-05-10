from helpers.args import COL_SIZE
from datetime import datetime


def check_line(line: list, line_num: int):
    fields = {
        '0': 'date',
        '1': 'int',
        '2': 'float',
        '3': 'str',
    }

    if not line or len(line) != COL_SIZE:
        raise Exception('Error parsing line {0}: {1}'.format(line_num, line))

    for i, value in enumerate(line):
        try:
            tp = fields.get(str(i))

            if tp == 'str':
                line[i] = str(value)
            elif tp == 'int':
                line[i] = int(value)
            elif tp == 'float':
                line[i] = float(value)
            elif tp == 'date':
                line[i] = datetime.strptime(value, "%Y-%m-%d")

        except Exception:
            raise TypeError(
                'Invalid type for line {0}, col {1}: {2}'.format(line_num, i, tp))

    return line
