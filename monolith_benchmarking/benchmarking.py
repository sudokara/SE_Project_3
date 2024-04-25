import numpy as np
import random
from datetime import datetime
from time import sleep
import os
import pickle

random.seed(42)


def write_random_char_to_file(file_path):
    # Open the file in write mode
    with open(file_path, 'a') as file:
        # Generate a random character
        random_char = chr(random.randint(32, 126))

        # Write the random character to the file
        file.write(random_char)

def clear_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as file:
        pass

def read_backup_time(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the whole file
        file_content = file.readline()
        print(file_content)

        # Extract the time from the file content
        backup_time_str = file_content.split(',')[0]
        print(backup_time_str)

        # Convert the string to a datetime object
        backup_time = datetime.strptime(backup_time_str, "%Y-%m-%d %H:%M:%S")

        return backup_time

time_list = []
for i in range(100):

    # clear_file(
    #     "/home/maggy/SE/project_3/SE_Project_3/src/phoenix/CLI/log")

    current_time = datetime.now()

    write_random_char_to_file(
        "/home/maggy/SE/project_3/SE_Project_3/src/phoenix/Observation/watchDir/watch2.txt")

    sleep(5)

    # backup_time = read_backup_time(
        # "/home/maggy/SE/project_3/SE_Project_3/src/phoenix/CLI/log")

    time_list.append(current_time)
    # print(current_time)
    # print((current_time - backup_time).total_seconds())
    # time_list.append(current_time)


# Save the array to a npy file
# np.save('/home/maggy/SE/project_3/SE_Project_3/time_list.npy', time_list)
with open('/home/maggy/SE/project_3/SE_Project_3/time_list.pkl', 'wb') as f:
    pickle.dump(time_list, f)