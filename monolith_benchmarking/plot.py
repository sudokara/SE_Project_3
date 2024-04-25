import pickle
from datetime import datetime

# Specify the path to the pickle file
file_path = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/benchmark_monolith/time_list.pkl'

# Open the pickle file in read mode
with open(file_path, 'rb') as file:
    # Load the data from the pickle file
    time_list = pickle.load(file)
# print(len(time_list))

# Now you can use the 'time_list' variable to access the data from the pickle file
bck_up_time = []
with open('/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/benchmark_monolith/log', 'r') as file:
    lines = file.readlines()
    # print(len(lines))
    for i in range(6, len(lines), 14):
        line = lines[i]
        # Assuming the time is at the start of the line and ends before the first space
        time_str = line.split(',')[0]
        time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        bck_up_time.append(time_obj)
# print(type(bck_up_time[0]))
# print(bck_up_time[0])
# print(type(time_list[0]))
# print(time_list[0])
        
# print(len(bck_up_time))
# now subtract every element of time_list from bck_up_time
diff = []
for i in range(len(time_list)):
    diff.append((bck_up_time[i] - time_list[i]).total_seconds())
# print(len(diff))

with open('diff.pkl', 'wb') as f:
    pickle.dump(diff, f)

# plot the diff using seaborn and very nicely

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
# sns.histplot(diff, kde=True, color="skyblue")
plt.plot(diff)
plt.title("Time taken for backup")
plt.xlabel("Request number")
plt.ylabel("Time taken (in seconds)")
plt.show()


for tim in time_list:
    print(tim.time().strftime("%H:%M:%S"))