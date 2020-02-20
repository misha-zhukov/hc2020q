from os import path
import os
from PriorityQueue import MaxPQ
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

        lib_score = []
        for i in range(0, n_libs):
            score = sum(map(lambda x: book_scores[x], lib_book_ids[i]))
            lib_score.append(score * lib_ship_books[i])

        lib_sort_indexes = sorted(
            range(len(lib_score)), key=lib_score.__getitem__)

        days_left = n_days
        zipped = zip(lib_score, lib_ids)
        sort = sorted(zipped, key=lambda x: x[0], reverse=False)

        lib_pq = MaxPQ()
        for k,v in sort:
            lib_pq.push(k, v)

        chosen_lib_id_book_n = []
        chosen_book_ids = []
        already_shipped_books = set()
        while days_left > 0 and len(lib_pq) > 0:
            lib_id = lib_pq.pop()
            days_left -= lib_signup_days[lib_id]
            if days_left <= 0:
                continue
            # lib_ship_books[lib_id] = [
            #     x for x in lib_ship_books[lib_id]]
            books_will_be_shipped = min(
                days_left * lib_ship_books[lib_id], lib_n_books[lib_id])

            chosen_book_ids.append(
                lib_book_ids[lib_id][:books_will_be_shipped])
            chosen_lib_id_book_n.append([lib_id, books_will_be_shipped])
            already_shipped_books.update(
                lib_book_ids[lib_id][:books_will_be_shipped])

            #TODO: update other libraries priorities reducing their score by the scores of the books taken
            # loop through books_added
            #   loop through libs_by_book[book]
            #       lib.score -= book.score
            #       lib_pq.push(lib.score, lib)

    # for day in range(0, n_days):

    return chosen_lib_id_book_n, chosen_book_ids


if __name__ == '__main__':
    filesHelper = FilesHelper()
    problems_dir_path = 'in'
    solutions_dir_path = 'out'

    problem_files = filesHelper.get_problem_files(problems_dir_path)
    # problem_files = ['a_example.txt']

    for file in problem_files:
        print(f'Start working on {file}')
        start_time = time.time()
        chosen_lib_id_book_n, chosen_book_ids = solve_file(
            path.join(os.getcwd(), problems_dir_path, file))
        with open(path.join(os.getcwd(), solutions_dir_path, file), 'w') as f:
            f.write(str(len(chosen_lib_id_book_n)) + '\n')
            for i in range(0, len(chosen_lib_id_book_n)):
                f.write(
                    str(chosen_lib_id_book_n[i][0]) + ' ' + str(chosen_lib_id_book_n[i][1]) + '\n')
                for j in range(0, len(chosen_book_ids[i])):
                    string = str(chosen_book_ids[i][j])
                    if j == len(chosen_book_ids[i])-1:
                        string += '\n'
                    else:
                        string += ' '
                    f.write(string)
        print(f'Finished working on {file}')
        print("--- %s seconds ---" % (time.time() - start_time))
