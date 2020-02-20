from os import path
import os
from FilesHelper import FilesHelper
from random import random
import time


def solve_file(filepath):
    with open(filepath) as fp:
        n_books, n_libs, n_days = [
            int(s) for s in fp.readline().rstrip('\n').split(" ")]
        book_scores = [int(s) for s in fp.readline().rstrip('\n').split(" ")]
        lib_n_books = []
        lib_signup_days = []
        lib_ship_books = []
        lib_book_ids = []
        lib_ids = []
        for i in range(0, n_libs):
            cur_lib_n_books, cur_lib_signup_days, cur_lib_ship_books = [
                int(s) for s in fp.readline().rstrip('\n').split(" ")]
            lib_n_books.append(cur_lib_n_books)
            lib_signup_days.append(cur_lib_signup_days)
            lib_ship_books.append(cur_lib_ship_books)
            cur_book_ids = [int(s)
                            for s in fp.readline().rstrip('\n').split(" ")]
            lib_book_ids.append(cur_book_ids)
            lib_ids.append(i)

    result = None
    return result


if __name__ == '__main__':
    filesHelper = FilesHelper()
    problems_dir_path = 'in'
    solutions_dir_path = 'out'

    # problem_files = filesHelper.get_problem_files(problems_dir_path)
    problem_files = ['a_example.txt']

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
