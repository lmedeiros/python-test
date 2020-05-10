Coded based on Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24)
// It runs on python 3.5.2 also //

***
    python = 'python3.8 executable at your os'
    run 'python -m unittest discover' to run all tests
    run 'python main.py' file on cli, it has argparse utils, it should be self explained.
    data folder has a valid example of csv to test
***


No external libs

Design pattern using pipeline, which implements separate each pipe that modifies the input, until it reaches the last pipe.

Helpers folder contains specific functions that helps the pipeline executes spare tasks.

Pipeline folder, has a pipeline manager, which contains logic to run from end to end the entire pipeline, passing the data through.

At the Pipes folder, it can be found the implementation of each pipe, making it simple and easy to make changes and test

Pipeline order and functions can be set at the class PipelineManager, it could be also at some metaprograming json object.

Added the argparse lib to help with the cli args, it can be located at helpers folder, args.

I looked forward to run loops over the lists minimum as possible, and also not to use pandas to group and parse the csv, to show off my skills. 

I would like to write more test cases, but I got a limited time, they are in the tests folder.