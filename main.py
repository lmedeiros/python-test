from helpers.args import (
    validate_date, validate_file, setup_argparser)

from pipeline.manager import PipelineManager

if __name__ == '__main__':
    parser = setup_argparser()
    args = parser.parse_args()

    if validate_date(args.max_date) and validate_file(args.src_file):
        pm = PipelineManager(args.src_file, args.max_date)
        pm.start()
