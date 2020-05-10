from models.pipe import Pipe
from .pipes import (load, output, summarize, validate)


class PipelineManager():

    pipeline = {
        'load': Pipe('load', 1, 'validate'),
        'validate': Pipe('validate', 2, 'summarize'),
        'summarize': Pipe('summarize', 3, 'output'),
        'output': Pipe('output', 4, None)
    }

    def __init__(self, src_file: str, max_date: str):
        self.step = 0

        self.src_file = src_file
        self.max_date = max_date
        self.raw_data = None

    @staticmethod
    def first_pipe() -> Pipe:
        for _, p in PipelineManager.pipeline.items():
            if p.position == 1:
                return p

    def __params_valid(self):
        if not self.src_file or not self.max_date:
            raise Exception(
                'File source or Max date were not provided to this pipeline')

    def send_next(self, pipe: Pipe):
        self.__params_valid()

        if pipe:
            self.raw_data = eval(pipe.func).run(
                self.raw_data, self.src_file, self.max_date)
            if pipe.next:
                next_pipe = PipelineManager.pipeline[pipe.next]
                self.send_next(next_pipe)
        else:
            raise Exception('Invalid pipeline step')

    def start(self):
        self.__params_valid()
        self.send_next(self.first_pipe())
