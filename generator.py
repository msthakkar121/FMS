import random
import string
from datetime import datetime

import schedule

import utils
from config import Conf


def generate_string(length):
    alphabets = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(alphabets) for i in range(length))
    return random_string


def generate_string_sequence():
    data = ''
    for i in range(Conf.SEQUENCE_LENGTH):
        random_string = generate_string(random.choice(Conf.STRING_LENGTHS))
        random_string = random.choices([random_string, Conf.DATA_CRITICAL_KEYWORD], weights=[0.5, 0.5])[0]
        data += random_string + ' '
    write_to_file(data)
    print(datetime.now(), ' - Written data to file.')


def write_to_file(data):
    file_name = random.choice([Conf.DATA_FILE_ONE, Conf.DATA_FILE_TWO])
    utils.check_file_size(file_name, Conf.DATA_DIRECTORY)
    file = open(Conf.DATA_DIRECTORY + '/' + file_name, 'a')

    file.write(str(datetime.now()) + '\n')
    file.write(data + '\n' * 2)

    file.close()


if __name__ == '__main__':
    print(f'Generator will write data sequence of length {Conf.SEQUENCE_LENGTH} '
          f'to output files every {Conf.GENERATOR_INTERVAL} seconds.')
    schedule.every(Conf.GENERATOR_INTERVAL).seconds.do(generate_string_sequence)
    while True:
        schedule.run_pending()
