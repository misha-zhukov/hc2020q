from os import path
import os
from FilesHelper import FilesHelper
from random import random
import time
import operator


class Lib:
    def __init__(self, signup_days, book_ids, ship_books, id, book_scores):
        self.signup_days = signup_days
        self.book_ids = book_ids
        self.ship_books = ship_books
        self.id = id
        self.score = 0
        self.sort_books(book_scores)

    def calc_score(self, book_scores):
        score = sum(map(lambda x: book_scores[x], self.book_ids))
        if len(self.book_ids) == 0:
            return
        mean_score = score/len(self.book_ids)
        self.score = mean_score * self.ship_books/self.signup_days

    def sort_books(self, book_scores):
        scores = map(lambda x: book_scores[x], self.book_ids)
        # lib_sort_indexes = sorted(
        #     range(len(lib_score)), key=lib_score.__getitem__)
        self.book_ids = [x for _, x in sorted(
            zip(book_scores, self.book_ids), reverse=True)]
        return self.book_ids


def get_max_lib(libs):
    max_lib = max(libs, key=operator.attrgetter('score'))
    return max_lib


def remove_scanned_books(libs, scanned_books):
    for lib in libs:
        lib.book_ids = [x for x in lib.book_ids if x not in scanned_books]


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
        libs = []
        for i in range(0, n_libs):
            cur_lib_n_books, cur_lib_signup_days, cur_lib_ship_books = [
                int(s) for s in fp.readline().rstrip('\n').split(" ")]
            lib_n_books.append(cur_lib_signup_days)
            lib_signup_days.append(cur_lib_signup_days)
            lib_ship_books.append(cur_lib_ship_books)
            cur_book_ids = [int(s)
                            for s in fp.readline().rstrip('\n').split(" ")]
            lib = Lib(cur_lib_signup_days, cur_book_ids,
                      cur_lib_ship_books, i, book_scores)
            lib_book_ids.append(cur_book_ids)
            lib_ids.append(i)
            libs.append(lib)

        days_left = n_days
        already_shipped_books = set()
        chosen_book_ids = []
        chosen_lib_id_book_n = []
        counter = 0
        while days_left > 0 and len(libs) > 0:
            for lib in libs:
                lib.calc_score(book_scores)
            counter += 1
            if counter % 10 == 0:
                print(counter)
            remove_scanned_books(libs, already_shipped_books)
            lib = get_max_lib(libs)
            days_left -= lib.signup_days
            if days_left <= 0:
                continue
            # lib_book_ids[lib_id] = [
            #     x for x in lib_book_ids[lib_id] if x not in already_shipped_books]
            if len(lib.book_ids) == 0:
                continue
            books_will_be_shipped = min(
                days_left * lib.ship_books, len(lib.book_ids))

            chosen_book_ids.append(
                lib.book_ids[:books_will_be_shipped])
            chosen_lib_id_book_n.append([lib.id, books_will_be_shipped])
            already_shipped_books.update(
                lib.book_ids[:books_will_be_shipped])
            libs.remove(lib)
    total_score = sum(map(lambda x: book_scores[x], [
        item for sublist in chosen_book_ids for item in sublist]))
    print(f'Estimated total score {total_score}')
    # for day in range(0, n_days):

    return chosen_lib_id_book_n, chosen_book_ids, total_score


if __name__ == '__main__':
    filesHelper = FilesHelper()
    problems_dir_path = 'in'
    solutions_dir_path = 'out'

    problem_files = filesHelper.get_problem_files(problems_dir_path)
    problem_files = ['a_example.txt', 'b_read_on.txt']
    total_total_score = 0
    for file in problem_files:
        print(f'Start working on {file}')
        start_time = time.time()

        chosen_lib_id_book_n, chosen_book_ids, total_score = solve_file(
            path.join(os.getcwd(), problems_dir_path, file))
        total_total_score += total_score
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
    print(f'Estimated total total score {total_total_score}')
