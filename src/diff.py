import difflib

def generate_git_diff(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()
    with open(file2_path, 'r') as file2:
        file2_lines = file2.readlines()

    diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file1_path, tofile=file2_path)
    return diff

# Example usage
file1_path = 'Observation/watch.txt'
file2_path = 'Observation/watch2.txt'
git_diff = generate_git_diff(file1_path, file2_path)
with open('diff.txt', 'w') as f:
    for line in git_diff:
        print(line, end='', file=f)

# apply the diff to file2
from difflib import unified_diff
with open(file2_path, 'r') as file2:
    file2_lines = file2.readlines()
diff = list(git_diff)
diff = diff[2:] # remove the first two lines
file2_lines = list(file2_lines)
file2_lines = file2_lines[:-1] # remove the last line
file2_lines = file2_lines + diff