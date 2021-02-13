import os
import shutil
from datetime import datetime


def check_file_size(file_name, path):
    # If file size > 10 MB, move it to Archives
    try:
        file_path = path + '/' + file_name
        file_size_in_KBs = os.stat(file_path).st_size / 1024
        if file_size_in_KBs > 10240:
            os.makedirs(path + '/Archives', exist_ok=True)
            new_file_path = path + '/Archives/' + file_name + '_' + str(datetime.now()) + '.txt'
            shutil.move(file_path, new_file_path)
    except OSError as e:
        # FileNotFoundError
        pass