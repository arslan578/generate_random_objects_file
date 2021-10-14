import random
import string
import os


def check_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def generate_random_objs_file(file):
    object_length = 10
    object_count = 0
    f = open(file, "w+")
    while True:
        random_obj = "{},{},{},{},".format(''.join(random.choices(string.ascii_uppercase, k=object_length)),
                                           ''.join(random.choices(string.digits, k=object_length)),
                                           ''.join(
                                               random.choices(string.ascii_uppercase + string.digits, k=object_length)),
                                           round(random.uniform(-999999, 9999999), 6))
        f.write(random_obj)
        object_count += 1
        if os.path.getsize(file) >= 2000000:
            break

    f.close()

    return object_count
