import os


class FilesHelper:
    def get_problem_files(self, problems_dir_path='in'):
        problem_files = self.list_files(problems_dir_path)
        print(f'Problem files: {problem_files}')
        return problem_files

    def get_solution_files(self, solutions_dir_path='out'):
        solution_files = self.list_files(solutions_dir_path)
        print(f'Solution files: {solution_files}')
        return solution_files

    def list_files(self, dir_path):
        file_name = [f for f in os.listdir(
            dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        return file_name

    def get_full_path(self, subdir, file):
        full_path = os.path.join(os.getcwd(), subdir, file)
        return full_path
