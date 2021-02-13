import re
from datetime import datetime

import schedule

import utils
from config import Conf


def search_file():
    data_file_names = [Conf.DATA_FILE_ONE, Conf.DATA_FILE_TWO]
    regex = r"\b" + Conf.SEARCH_CRITICAL_KEYWORD + r"\b"
    for data_file_name in data_file_names:
        count = 0
        for line in open(Conf.DATA_DIRECTORY + '/' + data_file_name):
            for match in re.finditer(regex, line):
                count += 1
        save_count(Conf.RESULTS_FILE, Conf.RESULTS_DIRECTORY, data_file_name, count)
    print(datetime.now(), ' - Search complete.')


def save_count(results_file_name, results_directory, data_file_name, count):
    utils.check_file_size(results_file_name, results_directory)

    file = open(results_directory + '/' + results_file_name, 'a')
    file.write(str(datetime.now()) + '\n')
    file.write(data_file_name + ' - ' + str(count) + '\n' * 2)
    file.close()


if __name__ == '__main__':
    print(f'System will search for the occurrence of {Conf.SEARCH_CRITICAL_KEYWORD} '
          f'in the files generated by the data sequence generator '
          f'every {Conf.SEARCH_INTERVAL} seconds.')
    schedule.every(Conf.SEARCH_INTERVAL).seconds.do(search_file)
    while True:
        schedule.run_pending()
