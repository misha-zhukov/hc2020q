from os import path
import os
from FilesHelper import FilesHelper
from random import random
import time


def solve_file(filepath):
    with open(filepath) as fp:
        N = int(fp.readline().rstrip('\n'))
        for i in range(0, N):
            data = [s for s in fp.readline().rstrip('\n').split(" ")]

    result = None
    return result


if __name__ == '__main__':
    filesHelper = FilesHelper()
    problems_dir_path = 'in'
    solutions_dir_path = 'out'

    problem_files = filesHelper.get_problem_files(problems_dir_path)
    problem_files = problem_files[0]

    for file in problem_files:
        print(f'Start working on {file}')
        start_time = time.time()
        result = solve_file(
            path.join(os.getcwd(), problems_dir_path, file))
        with open(path.join(os.getcwd(), solutions_dir_path, file), 'w') as f:
            f.write(str(len(out)) + '\n')
            for item in result:
                pass
        print(f'Finished working on {file}')
        print("--- %s seconds ---" % (time.time() - start_time))
