import pickle
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the path to the pickle file
file_path = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/microservice_benchmarking/time_list.pkl'

# Open the pickle file in read mode
with open(file_path, 'rb') as file:
    # Load the data from the pickle file
    time_list = pickle.load(file)

# print(len(time_list))
# Specify the path to the backup_time.txt file
backup_file_path = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/microservice_benchmarking/backup_time.txt'
# Open the backup_time.txt file in read mode
with open(backup_file_path, 'r') as backup_file:
    # Read lines from the file
    lines = backup_file.readlines()


bck_time_lst = []
for i in range(0, len(lines), 2):
# Convert time string to datetime object
    time_str = lines[i].strip()
    datetime_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')
    # Use the datetime object as needed
    print(datetime_obj)
    
    bck_time_lst.append(datetime_obj)


diff = []
for i in range(len(time_list)):
    diff.append((bck_time_lst[i] - time_list[i]).total_seconds())   

    # Dump diff to diff.pkl
diff_file_path = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/microservice_benchmarking/diff.pkl'
with open(diff_file_path, 'wb') as diff_file:
    pickle.dump(diff, diff_file)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
# sns.histplot(diff, kde=True, color="skyblue")
plt.plot(diff)
plt.title("Time taken for backup")
plt.xlabel("Request number")
plt.ylabel("Time taken (in seconds)")
plt.show()